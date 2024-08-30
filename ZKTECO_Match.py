from pyzkfp import ZKFP2
import sys
import os

sys.set_int_max_str_digits(1000_000)


zkfp = ZKFP2()
zkfp.Init()
zkfp.OpenDevice(0)
zkfp.Light("green")

first_image = None
def main():        
    while True:
        result = zkfp.AcquireFingerprint()
        if result is not None:
            files = os.listdir()
            scores = []
            names = []

            for file in files:
                try:
                    file.index('.bin')
                    f = open(file, "rb").read()
                    score = zkfp.DBMatch(f, result[0])
                    
                    scores.append(score)
                    names.append(file)
                except:
                    continue
            highest = max(scores)
            print(names[scores.index(highest)])
main()
# f.write(io.BytesIO(result[0]).read())
zkfp.CloseDevice()