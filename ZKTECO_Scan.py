from pyzkfp import ZKFP2
import sys
import time
import io

sys.set_int_max_str_digits(1000_000)


zkfp = ZKFP2()
zkfp.Init()
zkfp.OpenDevice(0)

first_image = None

while True:
    result = zkfp.AcquireFingerprint()
    if result is not None and first_image is None:

        first_image = result
        f = open(sys.argv[1]+".bin", "wb").write(bytearray(result[0]))
        # f.write(io.BytesIO(result[0]).read())
        # f.write(result[0])
        break

    # time.sleep(1000)
    # print('------------------')
    # result2 = zkfp.AcquireFingerprint()
    # if result2 is not None and first_image is not None:
    #     # print(int.from_bytes(result[1], byteorder='big'))
    #     # print(len(result[1]))
    #     # zkfp.show_image(result[1])
    #     # break
    #     print('case 2')
    #     print(zkfp.DBMatch(first_image[0], result2[0]))
    #     break


zkfp.CloseDevice()