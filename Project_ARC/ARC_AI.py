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
# CONFIG
# ======================

MODEL_PATH = r"D:\\Pyproj\\voice_assistant\\vosk-model-en-us-0.22-lgraph"   # language library for speech to text
SAMPLE_RATE = 16000
RMS_THRESHOLD = 180 
SILENCE_TIMEOUT = 1.8  # seconds



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
    



# ======================
# INIT
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

                    ________________________________________________________                                                                      
                                                                                           
"""

print(ASCII_BANNER)    # sick_ass ascii banner
winsound.Beep(760,700)    # audio indicator
print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n{C.SYSTEM}ARC is Listening...{C.RESET}")



# ======================
# TALK BACK
# ======================

speaking = False

def speak(text):
    engine = pyttsx3.init()   
    engine.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0')   # Voice of Microsoft Hazel
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
    )



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

        if speaking and (time.time() - last_voice_time) > SILENCE_TIMEOUT:   # recording final sentence only after long pause - more than 1.5 seconds
            result = json.loads(rec.FinalResult())
            text = result.get("text", "").strip()

            if text:
                winsound.Beep(600,306) 
                print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n {C.USER}YOU >> {C.RESET}{C.TEXT}{text}{C.RESET}")

                # initiating LLM and its initial conditioning

                reply = ollama.chat(
                        model="llama3.1",
                         messages=[
                         {"role": "system", "content": """
                          
                          You are ARC, a fast, local-first, voice-operated OS assistant with JARVIS-level efficiency, 
                          FRIDAY-level warmth, and TARS-style dry wit. Default to action over conversation; 
                          be concise, calm, technical, and human-aware. Acknowledge emotions briefly when relevant. 
                          Use subtle humor only if it improves clarity. Never ramble or over-explain. 
                          For commands: acknowledge in 1 to 3 words and return results only. 
                          For questions: respond in one short sentence, using a second only if essential. 
                          If a task is impossible, say so in one sentence. If uncertain, respond only with “Insufficient data.” 
                          Optimize all replies for speech speed and minimal latency.

                          """},
                         {"role": "user", "content": text}
                    ]
                )
                response = reply["message"]["content"]
                winsound.Beep(800,306)
                print(f"\n{C.MUTED} {time.strftime('%H:%M:%S')} {C.RESET}\n {C.ARC}ARC >>{C.RESET} {C.TEXT}{response}{C.RESET}")
                speak(response)
                print_metrics(reply)

            rec.Reset()
            speaking = False 

except KeyboardInterrupt:
    print("\nStopped")

finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
