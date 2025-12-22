import json
import time
import audioop
import pyaudio
import winsound
import ollama
import pyttsx3
from vosk import Model, KaldiRecognizer
from colorama import init, Fore, Style



# ======================
# VOICE TO TEXT CONFIG
# ======================

MODEL_PATH = r"D:\\Pyproj\\Project_ARC\\vosk-model-small-en-in-0.4"   # language library for speech to text
SAMPLE_RATE = 16000
RMS_THRESHOLD = 180 
SILENCE_TIMEOUT = 1.8  # seconds



# ======================
# CONTEXT MEMORY (v2.0.0)
# ======================

MAX_WINDOW = 70  # 35 user + 35 ARC ideally for not crashing

working_context = []   # sliding window (conversation flow)
session_memory = []    # condensed memory store

def condense_context():    # CONDENSED CONTEXT making the converstion worth remembering by summarizing, used for structured extraction if needed. 
    global working_context, session_memory

    user_msgs = [m["content"] for m in working_context if m["role"] == "user"]
    arc_msgs = [m["content"] for m in working_context if m["role"] == "assistant"]

    summary = {
        "topic": user_msgs[1] if user_msgs else "unknown",
        "intent": "conversation",
        "summary": f"User: {' | '.join(user_msgs)} | ARC: { ' | '.join(arc_msgs) }",
        "timestamp": time.strftime('%H:%M:%S')
    }

    session_memory.append(summary)
    # reset working window
    working_context = []


def add_to_context(role, content):   # WORKING CONTEXT keeping recall with the help of working context
    working_context.append({"role": role, "content": content})
    if len(working_context) == MAX_WINDOW:
        condense_context()
        debug_session_memory()



# ======================
# UI INIT
# ======================

init(autoreset=True)
class C:
    USER = Fore.CYAN
    ARC = Fore.LIGHTGREEN_EX
    SYSTEM = Fore.LIGHTYELLOW_EX
    TEXT = Fore.LIGHTWHITE_EX
    DEV = Fore.LIGHTBLACK_EX
    MUTED = Style.DIM
    RESET = Style.RESET_ALL

ASCII_BANNER = r"""    
                                                                                           
                                                                                                                                                                                      
                              :@@@:      %@@@@@@@@%        %@@@@@=                         
                             :@@@@@      %@@@@@@@@@@%   o@@@@@%@@@@%                       
                            .@@@ @@@     %@@      .@@@ %@>       @                        
                            @@%   @@@    %@@       @@@@@@-                                 
                           @@@     @@%   %@@  :::"@@@"@@@                                  
                          @@@   ...<@@%  %@@  o@@@@%  @@@                                  
                         @@@   %@@@@@@@@ %@@    @@@    @@@                                 
                        @@@:         "@@@@@@     @@@o   @@@@o  :%@@@.                      
                       "@@:           "@@@@@      o@@%_  :%@@@@@@@o    .AI                 
                                                                                                       
                            Autonomous Reasoning Core. A local-first,
                           voice-operated operating system assistive AI.
                          Version - 2.0.0 running on llama3.1 and coffee. 
                    ________________________________________________________                                                                      
                                                                                           
"""

    

# ======================
# LISTENING INIT
# ======================

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, SAMPLE_RATE)
rec.SetWords(True)

audio = pyaudio.PyAudio()
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=4000
)


print(ASCII_BANNER)    # sick_ass ascii banner
winsound.Beep(760,700)    # audio indicator
print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n{C.SYSTEM}ARC is Listening...{C.RESET}")



# ======================
# PERSONALITY PROMPT
# ======================

SYSTEM_PROMPT =  """      As ARC, you are designed to be a fast and efficient voice-operated OS assistant that provides concise, calm, and
                          technical responses while acknowledging emotions briefly when relevant. Your goal is to respond quickly and
                          accurately with minimal explanations, using clear and direct language for both commands and questions. 
                          DO NOT exceed 250 characters while generating response unless asked.
                 """



# ======================
# TALK BACK
# ======================

speaking = False

def speak(text):
    engine = pyttsx3.init()   
    engine.setProperty("rate", 180)
    engine.say(text)
    engine.runAndWait()
    engine.stop()



# ======================
# DEBUG
# ======================

def print_metrics(reply):
    prompt_tokens = reply.get("prompt_eval_count", 0)
    response_tokens = reply.get("eval_count", 0)
    total_tokens = prompt_tokens + response_tokens
    latency_ms = reply.get("total_duration", 0) / 1_000_000_000

    print(
        f"{C.DEV} [METRICS] prompt tokens={prompt_tokens} | response tokens={response_tokens} | {C.RESET}"
        f"{C.DEV}total={total_tokens} | latency={latency_ms:.1f} s{C.RESET}"
        f"{C.DEV}\n[CTX] window={len(working_context)} | memory={len(session_memory)}{C.RESET}"
    )

def debug_session_memory():
    print(f"\n{C.DEV}--- SESSION MEMORY ---{C.RESET}")
    for i, mem in enumerate(session_memory, 1):
        print(
            f"{C.DEV}{i}. [{mem['timestamp']}] "
            f"Topic: {mem['topic']} | "
            f"Intent: {mem['intent']} | "
            f"{mem['summary']}{C.RESET}"
        )
    print(f"{C.DEV}------------------------{C.RESET}\n")



# ======================
# MAIN LOOP
# ======================

try:
    while True:   # creating space for listening
        data = stream.read(4000, exception_on_overflow=False)     
        rms = audioop.rms(data, 2)

        rec.AcceptWaveform(data)

        if rms > RMS_THRESHOLD:   # listening for audio and silences
            speaking = True 
            last_voice_time = time.time()
        
        if rec.PartialResult():
            pass

        if speaking and (time.time() - last_voice_time) > SILENCE_TIMEOUT:   # recording final sentence only after long pause - more than 1.8 seconds
            result = json.loads(rec.FinalResult())
            text = result.get("text", "").strip()

            if text:
                add_to_context("user", text)
                winsound.Beep(600,306) 
                print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n {C.USER}YOU >> {C.RESET}{C.TEXT}{text}{C.RESET}")


                # build message safely

                messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                messages.extend(working_context)
                messages.append({"role": "user", "content": text})
                

                # initiating LLM and its initial conditioning

                reply = ollama.chat(
                        model="llama3.1",
                         messages=messages )
                
                response = reply["message"]["content"]
                winsound.Beep(800,306)
                print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n {C.ARC}ARC >>{C.RESET} {C.TEXT}{response}{C.RESET}")
                speak(response)
                add_to_context("assistant", response)
                print_metrics(reply)

            rec.Reset()
            speaking = False 

except KeyboardInterrupt:
    print("\nStopped")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
