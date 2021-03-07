import os
import time


def func(package_name, version_code_arry, target_arry):
    for i in range(len(version_code_arry)):
        build = version_code_arry[i][0]
        for patch in version_code_arry[i][1]:
            for target in target_arry:
                version_code = str(build).zfill(4) + \
                    str(patch).zfill(3) + \
                    str(target).zfill(2)

                os.popen('adb shell pm uninstall ' +
                         package_name + '_' + version_code)
                time.sleep(0.05)
    return


def main():
    arm_target_old = [3, 33, 43, 53, 8, 38, 48, 58]
    arm_target_new = [30, 33, 34, 35, 80, 83, 84, 85]
    intel_target_old = [13, 63, 73, 83, 18, 68, 78, 88]
    intel_target_new = [31, 36, 37, 38, 81, 86, 87, 88]

    func('com.google.android.trichromelibrary',
         version_code_stable_old, arm_target_old)  # 75~80

    func('com.google.android.trichromelibrary',
         version_code_stable_new, arm_target_new)  # 81~89

    func('com.google.android.trichromelibrary.beta',
         version_code_beta_old, arm_target_old)  # 75~80

    func('com.google.android.trichromelibrary.beta',
         version_code_beta_new, arm_target_new)  # 81~89

    return


version_code_stable_new = [
    [4389, [72]],  # 89
    [4324, [181, 152, 141, 93]],  # 88
    [4280, [141, 101, 86, 66]],  # 87
    [4240, [198, 185, 114, 110, 99, 75]],  # 86
    [4183, [127, 120, 101, 81]],  # 85
    [4147, [125, 111, 105, 89]],  # 84
    [4104, [106, 101, 96, 83, 60]],  # 83
    [4044, [138, 117, 111, 96]]  # 81
]


version_code_stable_old = [
    [3987, [162, 149, 132, 119, 117, 99, 87]],  # 80
    [3945, [136, 116, 93, 79]],  # 79
    [3904, [108, 96, 90, 62]],  # 78
    [3865, [116, 92, 73]],  # 77
    [3809, [132, 111, 89]],  # 76
    [3770, [143, 101, 89, 67]]  # 75
]


version_code_beta_new = [
    [4389, [72, 69, 57, 48, 35, 32, 23]],  # 89
    [4324, [93, 89, 79, 68, 51, 39, 38, 29]],  # 88
    [4280, [86, 66, 60, 49, 38, 27, 20]],  # 87
    [4240, [99, 75, 68, 52, 42, 30, 16]],  # 86
    [4183, [81, 78, 69, 59, 47, 38]],  # 85
    [4147, [89, 84, 69, 53, 44, 37, 27]],  # 84
    [4104, [83, 60, 56]],  # 83
    [4103, [44, 34, 23, 14]],  # 83
    [4044, [96, 91, 71, 66, 62, 42, 34, 26, 18]]  # 81
]


version_code_beta_old = [
    [3987, [99, 87, 78, 68, 58, 40, 18]],  # 80
    [3945, [79, 71, 56, 45, 36, 29, 18]],  # 79
    [3904, [62, 53, 43, 35, 18]],  # 78
    [3865, [92, 73, 66, 56, 42, 35, 18]],  # 77
    [3809, [89, 80, 70, 62, 45, 36, 21]],  # 76
    [3770, [89, 75, 67, 51, 40, 28, 16]]  # 75
]


if __name__ == '__main__':
    main()
    exit(0)
