#Sesleri kaydetmek için kullanılıyor
import pyaudio
import wave
def record_audio(filename, duration=5, sample_rate=44100, chunk=1024):
    audio= pyaudio.PyAudio()
    frames = []
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Kayıt başlıyor...")


    for i in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Kayıt tamamlandı.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.opem(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    #kullanım örneği
record_audio("kaydım.wav", duration=10)    
