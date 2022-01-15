import numpy as np
import matplotlib.pyplot as plt

env_map = [(2.32, 188.99), (4.64, 188.94), (6.96, 188.87), (9.27, 188.77), (11.59, 188.64), (13.9, 188.49), (16.22, 188.3), (18.62, 189.09), (20.94, 188.84), (23.26, 188.57), (25.57, 188.27), (28.03, 188.93), (30.34, 188.57), (32.65, 188.19), (34.96, 187.77), (37.26, 187.33), (39.56, 186.86), (42.29, 188.31), (44.59, 187.78), (47.14, 188.19), (49.19, 186.63), (50.94, 184.08), (51.53, 177.68), (51.96, 171.29), (54.06, 170.64), (56.78, 171.86), (59.21, 172.1), (60.98, 170.42), (60.28, 162.16), (59.02, 153.01), (58.3, 145.78), (57.79, 139.51), (57.52, 134.19), (57.14, 128.9), (55.8, 121.83), (53.44, 113.0), (53.95, 110.54), (55.3, 109.87), (57.11, 110.07), (58.45, 109.36), (60.27, 109.51), (62.11, 109.63), (63.95, 109.72), (65.81, 109.79), (67.67, 109.82), (69.55, 109.83), (70.89, 108.97), (71.11, 106.43), (70.72, 103.07), (70.25, 99.75), (70.3, 97.25), (69.7, 93.98), (69.63, 91.52), (69.52, 89.08), (69.36, 86.66), (69.15, 84.26), (68.89, 81.87), (68.58, 79.51), (68.89, 77.91), (68.5, 75.58), (68.06, 73.27), (68.26, 71.7), (67.74, 69.43), (67.88, 67.88), (67.99, 66.35), (68.08, 64.82), (68.14, 63.3), (68.17, 61.78), (67.42, 59.62), (67.39, 58.13), (68.1, 57.3), (67.25, 55.19), (66.36, 53.11), (56.76, 44.3), (49.34, 37.54), (49.0, 36.34), (49.44, 35.73), (49.06, 34.55), (49.48, 33.94), (49.89, 33.33), (50.29, 32.72), (49.85, 31.56), (50.23, 30.95), (50.61, 30.33), (50.11, 29.21), (49.59, 28.1), (49.94, 27.48), (50.27, 26.87), (49.71, 25.79), (49.13, 24.73), (49.43, 24.12), (48.82, 23.09), (49.1, 22.49), (48.45, 21.48), (48.71, 20.88), (48.97, 20.28), (49.21, 19.68), (48.52, 18.71), (48.74, 18.12), (48.96, 17.52), (48.23, 16.59), (48.43, 16.0), (48.62, 15.4), (48.8, 14.8), (48.98, 14.2), (48.19, 13.34), (48.35, 12.74), (47.53, 11.91), (47.67, 11.32), (48.79, 10.96), (47.94, 10.15), (48.06, 9.56), (48.17, 8.97), (48.28, 8.38), (48.38, 7.78), (48.47, 7.19), (47.56, 6.46), (47.64, 5.88), (47.71, 5.29), (47.77, 4.7), (47.82, 4.12), (47.87, 3.53), (47.91, 2.94), (46.94, 2.31), (46.97, 1.73), (47.99, 1.18), (47.0, 0.58), (48.0, 0.0), (47.0, -0.58), (46.99, -1.15), (46.97, -1.73), (46.94, -2.31), (46.91, -2.88), (46.87, -3.46), (46.83, -4.03), (46.77, -4.61), (46.71, -5.18), (46.65, -5.75), (46.57, -6.33), (46.49, -6.9), (47.39, -7.63), (47.29, -8.21), (46.21, -8.6), (47.08, -9.36), (46.96, -9.94), (46.83, -10.52), (46.7, -11.09), (46.56, -11.66), (46.41, -12.23), (46.26, -12.8), (46.1, -13.37), (45.93, -13.93), (46.71, -14.8), (46.53, -15.37), (46.33, -15.94), (47.08, -16.84), (45.93, -17.07), (45.72, -17.63), (46.43, -18.57), (46.19, -19.13), (45.96, -19.7), (45.71, -20.26), (45.46, -20.82), (46.1, -21.81), (45.83, -22.37), (45.55, -22.93), (46.16, -23.95), (45.86, -24.51), (45.56, -25.07), (46.11, -26.12), (45.79, -26.69), (45.46, -27.25), (45.12, -27.8), (45.62, -28.89), (45.26, -29.45), (45.73, -30.56), (45.35, -31.12), (44.97, -31.67), (45.39, -32.8), (44.98, -33.36), (45.36, -34.51), (45.72, -35.68), (44.5, -35.62), (45.61, -37.43), (45.14, -37.99), (45.43, -39.19), (44.95, -39.74), (45.2, -40.97), (44.69, -41.52), (44.9, -42.75), (45.09, -44.0), (45.25, -45.25), (45.39, -46.52), (45.51, -47.8), (44.92, -48.36), (44.99, -49.64), (44.38, -50.19), (41.8, -48.46), (39.92, -47.44), (38.7, -47.15), (37.49, -46.84), (36.91, -47.3), (36.33, -47.75), (36.34, -49.0), (36.32, -50.25), (35.7, -50.69), (35.08, -51.12), (35.0, -52.38), (34.9, -53.65), (34.77, -54.92), (34.62, -56.19), (35.47, -59.18), (35.25, -60.48), (35.0, -61.78), (34.72, -63.08), (34.41, -64.38), (36.38, -70.12), (123.64, -245.64), (173.25, -354.98), (197.1, -416.74), (206.55, -450.95), (220.05, -496.42), (229.3, -534.92), (231.52, -558.95), (226.13, -565.46), (215.22, -557.93), (208.7, -561.47), (196.74, -549.86), (177.62, -516.3), (166.88, -505.15), (157.04, -495.72), (143.11, -471.77), (133.97, -461.97), (131.22, -474.18), (130.49, -495.09), (117.85, -470.47), (99.12, -417.39), (95.97, -427.36), (94.44, -446.11), (85.84, -431.55), (83.65, -449.28), (87.02, -501.51), (86.42, -537.09), (86.28, -581.64), (80.75, -594.54), (72.71, -589.53), (66.02, -595.35), (59.5, -604.08), (52.34, -607.75), (44.73, -606.35), (36.06, -586.89), (27.04, -550.34), (21.75, -590.6), (14.95, -608.82), (7.49, -609.95), (0.0, -607.0), (-7.38, -600.95), (-14.68, -597.82), (-21.86, -593.6), (-28.02, -570.31), (-34.71, -564.93), (-43.18, -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                585.41), (-50.79, -589.82), (-57.34, -582.18), (-59.74, -538.7), (-66.35, -537.92), (-78.19, -575.71), (-83.78, -564.82), (-90.87, -564.74), (-101.89, -587.23), (-110.01, -590.85), (-117.44, -590.43), (-125.92, -594.82), (-133.87, -596.15), (-141.87, -597.39), (-150.89, -602.39), (-159.04, -603.39), (-149.09, -538.75), (-132.3, -456.2), (-135.56, -446.89), (-141.64, -447.1), (-152.45, -461.47), (-162.98, -473.75), (-142.5, -398.27), (-133.44, -359.0), (-132.08, -342.41), (-121.79, -304.55), (-60.85, -146.9), (-53.98, -125.92), (-53.9, -121.59), (-53.72, -117.28), (-51.73, -109.38), (-51.32, -105.14), (-51.71, -102.72), (-51.12, -98.53), (-50.91, -95.25), (-50.63, -91.99), (-50.28, -88.75), (-49.85, -85.53), (-49.87, -83.2), (-49.31, -80.03), (-48.68, -76.88), (-41.44, -63.71), (-39.45, -59.03), (-39.6, -57.72), (-39.15, -55.6), (-39.25, -54.3), (-39.32, -53.01), (-38.75, -50.93), (-38.76, -49.67), (-38.74, -48.41), (-38.7, -47.15), (-38.63, -45.91), (-39.19, -45.43), (-39.74, -44.95), (-39.62, -43.72), (-39.47, -42.49), (-39.3, -41.28), (-38.41, -39.37), (-37.48, -37.48), (-35.79, -34.92), (-35.49, -33.79), (-35.9, -33.35), (-34.82, -31.56), (-35.21, -31.13), (-34.83, -30.05), (-35.2, -29.62), (-34.79, -28.55), (-34.35, -27.49), (-33.9, -26.45), (-34.22, -26.04), (-33.73, -25.02), (-34.04, -24.6), (-33.52, -23.61), (-33.81, -23.2), (-33.26, -22.22), (-32.69, -21.27), (-32.95, -20.86), (-32.35, -19.93), (-32.59, -19.54), (-31.97, -18.63), (-31.32, -17.74), (-31.54, -17.36), (-31.75, -16.97), (-31.07, -16.12), (-31.26, -15.74), (-31.45, -15.35), (-31.64, -14.96), (-30.91, -14.16), (-31.08, -13.78), (-30.33, -13.0), (-30.49, -12.63), (-30.64, -12.25), (-29.86, -11.52), (-29.99, -11.15), (-30.13, -10.78), (-29.31, -10.08), (-29.44, -9.72), (-29.55, -9.36), (-29.67, -9.0), (-29.77, -8.63), (-29.88, -8.27), (-29.01, -7.65), (-29.1, -7.29), (-29.19, -6.93), (-28.3, -6.35), (-28.37, -6.01), (-28.44, -5.66), (-28.51, -5.31), (-28.57, -4.96), (-28.63, -4.61), (-28.69, -4.26), (-28.74, -3.9), (-27.79, -3.43), (-27.83, -3.09), (-27.87, -2.74), (-27.9, -2.4), (-27.92, -2.06), (-27.95, -1.72), (-27.97, -1.37), (-27.98, -1.03), (-27.99, -0.69), (-28.0, -0.34), (-28.0, -0.0), (-28.0, 0.34), (-27.99, 0.69), (-27.98, 1.03), (-27.97, 1.37), (-27.95, 1.72), (-27.92, 2.06), (-26.9, 2.32), (-26.87, 2.65), (-27.83, 3.09), (-26.8, 3.31), (-27.75, 3.77), (-26.71, 3.96), (-27.64, 4.45), (-27.59, 4.79), (-27.53, 5.13), (-27.46, 5.46), (-27.39, 5.8), (-27.32, 6.13), (-27.24, 6.47), (-27.16, 6.8), (-27.08, 7.14), (-26.99, 7.47), (-26.89, 7.8), (-26.79, 8.13), (-26.69, 8.46), (-26.59, 8.78), (-26.48, 9.11), (-26.36, 9.43), (-26.25, 9.76), (-26.12, 10.08), (-26.0, 10.4), (-26.79, 11.1), (-26.65, 11.43), (-26.51, 11.75), (-26.37, 12.08), (-26.22, 12.4), (-26.06, 12.72), (-25.9, 13.04), (-25.74, 13.36), (-26.46, 14.14), (-26.28, 14.47), (-26.1, 14.79), (-25.92, 15.11), (-25.73, 15.42), (-25.54, 15.74), (-26.19, 16.58), (-25.98, 16.91), (-25.78, 17.22), (-25.56, 17.54), (-25.35, 17.85), (-25.93, 18.75), (-25.7, 19.06), (-25.47, 19.38), (-25.23, 19.69), (-25.76, 20.62), (-25.51, 20.93), (-25.25, 21.25), (-25.75, 22.21), (-25.47, 22.52), (-25.19, 22.83), (-25.64, 23.82), (-25.35, 24.13), (-25.05, 24.44), (-25.46, 25.46), (-25.14, 25.77), (-24.82, 26.07), (-25.18, 27.11), (-24.85, 27.42), (-24.51, 27.72), (-24.82, 28.77), (-25.11, 29.84), (-24.74, 30.15), (-24.99, 31.23), (-25.22, 32.32), (-24.83, 32.63), (-24.42, 32.93), (-24.6, 34.04), (-24.76, 35.16), (-27.72, 40.4), (-35.0, 52.38), (-39.81, 61.19), (-39.59, 62.52), (-39.34, 63.85), (-39.07, 65.19), (-39.28, 67.39), (-38.94, 68.74), (-39.06, 70.96), (-38.65, 72.32), (-38.69, 74.56), (-38.67, 76.82), (-38.6, 79.08), (-38.48, 81.36), (-38.31, 83.64), (-38.09, 85.94), (-38.22, 89.15), (-37.5, 90.54), (-37.87, 94.71), (-37.79, 97.96), (-36.93, 99.36), (-35.71, 99.8), (-34.48, 100.23), (-36.7, 111.09), (-38.66, 122.02), (-38.32, 126.32), (-38.16, 131.58), (-37.87, 136.86), (-37.47, 142.15), (-37.18, 148.41), (-36.97, 155.67), (-36.59, 162.94), (-34.79, 164.36), (-32.97, 165.75), (-31.3, 168.11), (-29.41, 169.47), (-21.76, 135.26), (-16.73, 112.77), (-15.21, 111.97), (-13.83, 112.15), (-12.46, 112.31), (-11.86, 120.42), (-16.3, 189.3), (-14.12, 191.48), (-11.77, 191.64), (-9.42, 191.77), (-7.07, 191.87), (-4.69, 190.94), (-2.34, 190.99), (-0.0, 191.0)]

x = [x[0] for x in env_map]
y = [y[1] for y in env_map]

plt.scatter(x, y)
plt.show()
