import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np

date,bid,ask = np.loadtxt('../GBPUSD1d.txt',
                              unpack=True,
                              delimiter=',',
                              converters={0: mdates.bytespdate2num("%Y%m%d%H%M%S")})

def percent_change(start, current):
    default_zero_handler = 0.0000000001
    try:
        result = ((current - start) / abs(float(start))) * 100
        if result == 0.0:
            return default_zero_handler
        else:
            return result
    except:
        return default_zero_handler

def pattern_storage():
    start_time = time.time()
    x = len(avg_line) - 60
    y = 31

    while y < x:
        pattern = []
        p1  = percent_change(avg_line[y-30], avg_line[y-29])
        p2  = percent_change(avg_line[y-30], avg_line[y-28])
        p3  = percent_change(avg_line[y-30], avg_line[y-27])
        p4  = percent_change(avg_line[y-30], avg_line[y-26])
        p5  = percent_change(avg_line[y-30], avg_line[y-25])
        p6  = percent_change(avg_line[y-30], avg_line[y-24])
        p7  = percent_change(avg_line[y-30], avg_line[y-23])
        p8  = percent_change(avg_line[y-30], avg_line[y-22])
        p9  = percent_change(avg_line[y-30], avg_line[y-21])
        p10 = percent_change(avg_line[y-30], avg_line[y-20])

        p11 = percent_change(avg_line[y-30], avg_line[y-19])
        p12 = percent_change(avg_line[y-30], avg_line[y-18])
        p13 = percent_change(avg_line[y-30], avg_line[y-17])
        p14 = percent_change(avg_line[y-30], avg_line[y-16])
        p15 = percent_change(avg_line[y-30], avg_line[y-15])
        p16 = percent_change(avg_line[y-30], avg_line[y-14])
        p17 = percent_change(avg_line[y-30], avg_line[y-13])
        p18 = percent_change(avg_line[y-30], avg_line[y-12])
        p19 = percent_change(avg_line[y-30], avg_line[y-11])
        p20 = percent_change(avg_line[y-30], avg_line[y-10])

        p21 = percent_change(avg_line[y-30], avg_line[y-9])
        p22 = percent_change(avg_line[y-30], avg_line[y-8])
        p23 = percent_change(avg_line[y-30], avg_line[y-7])
        p24 = percent_change(avg_line[y-30], avg_line[y-6])
        p25 = percent_change(avg_line[y-30], avg_line[y-5])
        p26 = percent_change(avg_line[y-30], avg_line[y-4])
        p27 = percent_change(avg_line[y-30], avg_line[y-3])
        p28 = percent_change(avg_line[y-30], avg_line[y-2])
        p29 = percent_change(avg_line[y-30], avg_line[y-1])
        p30 = percent_change(avg_line[y-30], avg_line[y])

        outcome_range = avg_line[y+20:y+30]
        average_outcome = float(sum(outcome_range)) / len(outcome_range)
        current_point = avg_line[y]

        future_outcome = percent_change(current_point, average_outcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)
        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        patterns.append(pattern)
        performances.append(future_outcome)

        y += 1


    end_time = time.time()

    print(len(patterns))
    print(len(performances))
    print("Pattern storage took", end_time - start_time, "seconds.")


def current_pattern():
    current_pattern_1  = percent_change(avg_line[-31], avg_line[-30])
    current_pattern_2  = percent_change(avg_line[-31], avg_line[-29])
    current_pattern_3  = percent_change(avg_line[-31], avg_line[-28])
    current_pattern_4  = percent_change(avg_line[-31], avg_line[-27])
    current_pattern_5  = percent_change(avg_line[-31], avg_line[-26])
    current_pattern_6  = percent_change(avg_line[-31], avg_line[-25])
    current_pattern_7  = percent_change(avg_line[-31], avg_line[-24])
    current_pattern_8  = percent_change(avg_line[-31], avg_line[-23])
    current_pattern_9  = percent_change(avg_line[-31], avg_line[-22])
    current_pattern_10 = percent_change(avg_line[-31], avg_line[-21])
    current_pattern_11 = percent_change(avg_line[-31], avg_line[-20])
    current_pattern_12 = percent_change(avg_line[-31], avg_line[-19])
    current_pattern_13 = percent_change(avg_line[-31], avg_line[-18])
    current_pattern_14 = percent_change(avg_line[-31], avg_line[-17])
    current_pattern_15 = percent_change(avg_line[-31], avg_line[-16])
    current_pattern_16 = percent_change(avg_line[-31], avg_line[-15])
    current_pattern_17 = percent_change(avg_line[-31], avg_line[-14])
    current_pattern_18 = percent_change(avg_line[-31], avg_line[-13])
    current_pattern_19 = percent_change(avg_line[-31], avg_line[-12])
    current_pattern_20 = percent_change(avg_line[-31], avg_line[-11])
    current_pattern_21 = percent_change(avg_line[-31], avg_line[-10])
    current_pattern_22 = percent_change(avg_line[-31], avg_line[-9])
    current_pattern_23 = percent_change(avg_line[-31], avg_line[-8])
    current_pattern_24 = percent_change(avg_line[-31], avg_line[-7])
    current_pattern_25 = percent_change(avg_line[-31], avg_line[-6])
    current_pattern_26 = percent_change(avg_line[-31], avg_line[-5])
    current_pattern_27 = percent_change(avg_line[-31], avg_line[-4])
    current_pattern_28 = percent_change(avg_line[-31], avg_line[-3])
    current_pattern_29 = percent_change(avg_line[-31], avg_line[-2])
    current_pattern_30 = percent_change(avg_line[-31], avg_line[-1])

    pattern_to_recognize.append(current_pattern_1)
    pattern_to_recognize.append(current_pattern_2)
    pattern_to_recognize.append(current_pattern_3)
    pattern_to_recognize.append(current_pattern_4)
    pattern_to_recognize.append(current_pattern_5)
    pattern_to_recognize.append(current_pattern_6)
    pattern_to_recognize.append(current_pattern_7)
    pattern_to_recognize.append(current_pattern_8)
    pattern_to_recognize.append(current_pattern_9)
    pattern_to_recognize.append(current_pattern_10)
    pattern_to_recognize.append(current_pattern_11)
    pattern_to_recognize.append(current_pattern_12)
    pattern_to_recognize.append(current_pattern_13)
    pattern_to_recognize.append(current_pattern_14)
    pattern_to_recognize.append(current_pattern_15)
    pattern_to_recognize.append(current_pattern_16)
    pattern_to_recognize.append(current_pattern_17)
    pattern_to_recognize.append(current_pattern_18)
    pattern_to_recognize.append(current_pattern_19)
    pattern_to_recognize.append(current_pattern_20)
    pattern_to_recognize.append(current_pattern_21)
    pattern_to_recognize.append(current_pattern_22)
    pattern_to_recognize.append(current_pattern_23)
    pattern_to_recognize.append(current_pattern_24)
    pattern_to_recognize.append(current_pattern_25)
    pattern_to_recognize.append(current_pattern_26)
    pattern_to_recognize.append(current_pattern_27)
    pattern_to_recognize.append(current_pattern_28)
    pattern_to_recognize.append(current_pattern_29)
    pattern_to_recognize.append(current_pattern_30)

    print(pattern_to_recognize)

def pattern_recognition():
    predicted_outcomes = []
    pattern_found = 0
    patterns_to_plot = []

    for pattern in patterns:
        similarity0 = 100.0 - abs(percent_change(pattern[0], pattern_to_recognize[0]))
        similarity1 = 100.0 - abs(percent_change(pattern[1], pattern_to_recognize[1]))
        similarity2 = 100.0 - abs(percent_change(pattern[2], pattern_to_recognize[2]))
        similarity3 = 100.0 - abs(percent_change(pattern[3], pattern_to_recognize[3]))
        similarity4 = 100.0 - abs(percent_change(pattern[4], pattern_to_recognize[4]))
        similarity5 = 100.0 - abs(percent_change(pattern[5], pattern_to_recognize[5]))
        similarity6 = 100.0 - abs(percent_change(pattern[6], pattern_to_recognize[6]))
        similarity7 = 100.0 - abs(percent_change(pattern[7], pattern_to_recognize[7]))
        similarity8 = 100.0 - abs(percent_change(pattern[8], pattern_to_recognize[8]))
        similarity9 = 100.0 - abs(percent_change(pattern[9], pattern_to_recognize[9]))

        similarity10 = 100.0 - abs(percent_change(pattern[10], pattern_to_recognize[10]))
        similarity11 = 100.0 - abs(percent_change(pattern[11], pattern_to_recognize[11]))
        similarity12 = 100.0 - abs(percent_change(pattern[12], pattern_to_recognize[12]))
        similarity13 = 100.0 - abs(percent_change(pattern[13], pattern_to_recognize[13]))
        similarity14 = 100.0 - abs(percent_change(pattern[14], pattern_to_recognize[14]))
        similarity15 = 100.0 - abs(percent_change(pattern[15], pattern_to_recognize[15]))
        similarity16 = 100.0 - abs(percent_change(pattern[16], pattern_to_recognize[16]))
        similarity17 = 100.0 - abs(percent_change(pattern[17], pattern_to_recognize[17]))
        similarity18 = 100.0 - abs(percent_change(pattern[18], pattern_to_recognize[18]))
        similarity19 = 100.0 - abs(percent_change(pattern[19], pattern_to_recognize[19]))

        similarity20 = 100.0 - abs(percent_change(pattern[20], pattern_to_recognize[20]))
        similarity21 = 100.0 - abs(percent_change(pattern[21], pattern_to_recognize[21]))
        similarity22 = 100.0 - abs(percent_change(pattern[22], pattern_to_recognize[22]))
        similarity23 = 100.0 - abs(percent_change(pattern[23], pattern_to_recognize[23]))
        similarity24 = 100.0 - abs(percent_change(pattern[24], pattern_to_recognize[24]))
        similarity25 = 100.0 - abs(percent_change(pattern[25], pattern_to_recognize[25]))
        similarity26 = 100.0 - abs(percent_change(pattern[26], pattern_to_recognize[26]))
        similarity27 = 100.0 - abs(percent_change(pattern[27], pattern_to_recognize[27]))
        similarity28 = 100.0 - abs(percent_change(pattern[28], pattern_to_recognize[28]))
        similarity29 = 100.0 - abs(percent_change(pattern[29], pattern_to_recognize[29]))

        how_similar = (similarity0 + similarity1 + similarity2 + similarity3 + similarity4 + similarity5 + similarity6 + similarity7 + similarity8 + similarity9 + similarity10 + similarity11 + similarity12 + similarity13 + similarity14 + similarity15 + similarity16 + similarity17 + similarity18 + similarity19 + similarity20 + similarity21 + similarity22 + similarity23 + similarity24 + similarity25 + similarity26 + similarity27 + similarity28 + similarity29) / 30.00

        if how_similar > 70:
            patdex = patterns.index(pattern)

            pattern_found = 1

            # print('############################')
            # print('############################')
            # print(pattern_to_recognize)
            # print('============================')
            # print('============================')
            # print(pattern)
            # print('----------------------------')
            # print('Predicted Outcome: ', performances[patdex])
            xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

            patterns_to_plot.append(pattern)

    if pattern_found == 1:
        fig = plt.figure(figsize=(10,6))

        for pattern in patterns_to_plot:
            future_points = patterns.index(pattern)

            if performances[future_points] > pattern_to_recognize[29]:
                p_color = '#24bc00'
            else:
                p_color = '#d40000'

            plt.plot(xp, pattern)
            predicted_outcomes.append(performances[future_points])

            plt.scatter(35, performances[future_points], c=p_color, alpha=.3)

        real_outcome_range = all_data[to_what+20:to_what+30]
        real_avg_outcome = float(sum(real_outcome_range)) / len(real_outcome_range)
        real_movement = percent_change(all_data[to_what], real_avg_outcome)

        predicted_average_outcome = float(sum(predicted_outcomes)) / len(predicted_outcomes)

        plt.scatter(40, real_movement, c='#54fff7', s=25)
        plt.scatter(40, predicted_average_outcome, c='b', s=25)

        plt.plot(xp, pattern_to_recognize, '#54fff7', linewidth=3)
        plt.grid(True)
        plt.title('Pattern Recognition')
        plt.show()


data_length = int(bid.shape[0])
print('Length of data: ', data_length)

# add the elements of two arrays and divide each by 2 => average of bid and ask
all_data = ((bid + ask) / 2)
to_what = 37000

while to_what < data_length:
    avg_line = all_data[:to_what]
    patterns = []
    performances = []
    pattern_to_recognize = []


    pattern_storage()
    print("Getting current pattern...")
    current_pattern()
    pattern_recognition()

    move_forward = input('Press ENTER to continue.')
    to_what += 1
