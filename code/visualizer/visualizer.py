import matplotlib.pyplot as plt

env_map = [(7.16, 227.89, 227.99999999999997, 1.8), (14.32, 227.55, 227.99999999999997, 3.6), (21.46, 226.99, 227.99999999999997, 5.4), (28.7, 227.19, 229.0, 7.2), (35.82, 226.18, 229.0, 9.0), (43.1, 225.93, 229.99999999999997, 10.8), (50.39, 225.44, 231.0, 12.600000000000001), (57.7, 224.71, 231.99999999999997, 14.400000000000002), (65.28, 224.71, 234.0, 16.200000000000003), (72.62, 223.5, 235.0, 18.000000000000004), (80.62, 223.93, 238.0, 19.800000000000004), (88.35, 223.15, 240.0, 21.600000000000005), (96.51, 223.01, 243.00000000000003, 23.400000000000006), (104.74, 222.59, 246.0, 25.200000000000006), (113.04, 221.86, 249.00000000000003, 27.000000000000007), (121.88, 221.71, 252.99999999999997, 28.800000000000008), (129.81, 219.49, 254.99999999999997, 30.60000000000001), (137.71, 216.99, 257.0, 32.400000000000006), (144.46, 212.56, 257.0, 34.2), (138.13, 190.12, 235.0, 36.0), (133.0, 171.46, 217.0, 37.8), (131.95, 159.5, 206.99999999999997, 39.599999999999994), (130.94, 148.52, 198.0, 41.39999999999999), (129.38, 137.78, 189.0, 43.19999999999999), (127.28, 127.28, 180.0, 44.999999999999986), (127.57, 119.8, 175.0, 46.79999999999998), (126.77, 111.76, 169.0, 48.59999999999998), (126.36, 104.54, 164.0, 50.39999999999998), (129.59, 100.52, 164.0, 52.199999999999974), (137.53, 99.92, 170.0, 53.99999999999997), (145.57, 98.93, 176.0, 55.79999999999997), (154.51, 98.06, 183.0, 57.599999999999966), (151.49, 89.59, 176.0, 59.39999999999996), (130.57, 71.78, 149.0, 61.19999999999996), (115.83, 59.02, 130.0, 62.99999999999996), (115.82, 54.5, 128.0, 64.79999999999995), (114.72, 49.64, 125.0, 66.59999999999995), (114.36, 45.28, 123.0, 68.39999999999995), (113.85, 40.99, 121.0, 70.19999999999995), (113.18, 36.77, 119.0, 71.99999999999994), (113.31, 32.92, 118.0, 73.79999999999994), (29841.08, 7661.89, 30808.999999999996, 75.59999999999994), (121.99, 27.27, 125.0, 77.39999999999993), (140.47, 26.8, 143.0, 79.19999999999993), (171.86, 27.22, 174.0, 80.99999999999993), (184.53, 23.31, 186.0, 82.79999999999993), (184.18, 17.41, 185.0, 84.59999999999992), (182.64, 11.49, 183.0, 86.39999999999992), (182.91, 5.75, 183.0, 88.19999999999992), (182.0, 0.0, 182.0, 89.99999999999991), (181.91, -5.72, 182.0, 91.79999999999991), (180.64, -11.37, 181.0, 93.59999999999991), (180.2, -17.03, 181.0, 95.3999999999999), (179.57, -22.69, 181.0, 97.1999999999999), (179.76, -28.47, 182.0, 98.9999999999999), (178.78, -34.1, 182.0, 100.7999999999999), (178.59, -39.92, 183.0, 102.5999999999999), (178.22, -45.76, 184.0, 104.39999999999989), (177.65, -51.61, 185.0, 106.19999999999989), (176.9, -57.48, 186.0, 107.99999999999989), (181.59, -65.38, 193.0, 109.79999999999988), (211.99, -83.93, 227.99999999999997, 111.59999999999988), (228.52, -98.89, 249.00000000000003, 113.39999999999988), (265.11, -124.75, 293.0, 115.19999999999987), (269.08, -137.11, 302.0, 116.99999999999987), (259.39, -142.6, 296.0, 118.79999999999987), (239.29, -141.51, 278.0, 120.59999999999987), (232.19, -147.35, 275.0, 122.39999999999986), (0.0, -0.0, 0.0, 124.19999999999986), (254.84, -185.15, 315.0, 125.99999999999986), (255.22, -197.97, 323.0, 127.79999999999986), (231.92, -191.86, 301.0, 129.59999999999985), (222.78, -196.41, 297.0, 131.39999999999986), (223.06, -209.47, 306.0, 133.19999999999987), (200.82, -200.82, 284.0, 134.9999999999999), (156.08, -166.2, 227.99999999999997, 136.7999999999999), (148.13, -168.02, 224.00000000000003, 138.5999999999999), (160.63, -194.17, 252.0, 140.39999999999992), (168.55, -217.29, 275.0, 142.19999999999993), (157.53, -216.82, 268.0, 143.99999999999994), (147.27, -216.7, 262.0, 145.79999999999995), (129.67, -204.33, 242.0, 147.59999999999997), (97.74, -165.26, 192.0, 149.39999999999998), (82.38, -149.85, 171.0, 151.2), (75.82, -148.8, 167.0, 153.0), (80.05, -170.11, 188.0, 154.8), (90.55, -209.25, 227.99999999999997, 156.60000000000002), (83.93, -211.99, 227.99999999999997, 158.40000000000003), (76.22, -211.7, 225.0, 160.20000000000005), (68.29, -210.18, 221.0, 162.00000000000006), (61.1, -210.3, 219.0, 163.80000000000007), (53.47, -208.25, 215.0, 165.60000000000008), (43.63, -195.18, 200.0, 167.4000000000001), (31.29, -164.04, 167.0, 169.2000000000001), (24.56, -155.07, 157.0, 171.0000000000001), (18.05, -142.86, 144.0, 172.80000000000013), (13.27, -140.37, 141.0, 174.60000000000014), (8.85, -140.72, 141.0, 176.40000000000015), (4.62, -146.93, 147.0, 178.20000000000016), (-0.0, -182.0, 182.0, 180.00000000000017), (-6.44, -204.9, 204.99999999999997, 181.80000000000018), (-12.75, -202.6, 202.99999999999997, 183.6000000000002), (-18.92, -200.11, 200.99999999999997, 185.4000000000002), (-25.19, -199.42, 200.99999999999997, 187.20000000000022), (-31.44, -198.53, 200.99999999999997, 189.00000000000023), (-37.85, -198.42, 202.0, 190.80000000000024), (-44.28, -198.11, 202.99999999999997, 192.60000000000025), (-50.73, -197.59, 204.0, 194.40000000000026), (-57.19, -196.86, 204.99999999999997, 196.20000000000027), (-63.66, -195.92, 206.0, 198.00000000000028), (-70.46, -195.7, 208.0, 199.8000000000003), (-77.31, -195.25, 210.0, 201.6000000000003), (-84.59, -195.48, 213.0, 203.40000000000032), (-91.54, -194.54, 215.0, 205.20000000000033), (-99.42, -195.13, 219.0, 207.00000000000034), (-108.39, -197.17, 225.0, 208.80000000000035), (-114.53, -193.67, 225.0, 210.60000000000036), (-113.6, -179.0, 212.0, 212.40000000000038), (-112.42, -165.42, 200.0, 214.2000000000004), (-110.5, -152.1, 188.0, 216.0000000000004), (-109.71, -141.44, 179.0, 217.8000000000004), (-108.36, -130.99, 170.0, 219.60000000000042), (-107.79, -122.27, 163.0, 221.40000000000043), (-106.79, -113.72, 156.0, 223.20000000000044), (-106.07, -106.07, 150.0, 225.00000000000045), (-104.97, -98.57, 144.0, 226.80000000000047), (-104.27, -91.92, 139.0, 228.60000000000048), (-104.02, -86.05, 135.0, 230.4000000000005), (-103.51, -80.29, 131.0, 232.2000000000005), (-104.36, -75.82, 129.0, 234.0000000000005), (-107.52, -73.07, 130.0, 235.80000000000052), (-102.16, -64.84, 121.0, 237.60000000000053), (-99.85, -59.05, 115.99999999999999, 239.40000000000055), (-99.9, -54.92, 113.99999999999999, 241.20000000000056), (-99.79, -50.85, 112.00000000000001, 243.00000000000057), (-99.53, -46.84, 110.00000000000001, 244.80000000000058), (-99.12, -42.89, 108.0, 246.6000000000006), (-98.56, -39.02, 106.0, 248.4000000000006), (-97.85, -35.23, 104.0, 250.2000000000006), (-97.96, -31.83, 103.0, 252.00000000000063), (-103.71, -30.13, 108.0, 253.80000000000064), (-116.23, -29.84, 120.0, 255.60000000000065), (-131.75, -29.45, 135.0, 257.40000000000066), (-149.31, -28.48, 152.0, 259.20000000000067), (-157.04, -24.87, 159.0, 261.0000000000007), (-156.75, -19.8, 158.0, 262.8000000000007), (-151.33, -14.3, 152.0, 264.6000000000007), (-147.71, -9.29, 148.0, 266.4000000000007), (-145.93, -4.59, 146.0, 268.2000000000007), (-145.0, 0.0, 145.0, 270.00000000000074), (-134.93, 4.24, 135.0, 271.80000000000075), (-125.75, 7.91, 126.0, 273.60000000000076), (-121.46, 11.48, 122.0, 275.4000000000008), (-63.5, 8.02, 64.0, 277.2000000000008), (-30.62, 4.85, 31.0, 279.0000000000008), (-44.2, 8.43, 45.0, 280.8000000000008), (-108.33, 24.21, 111.00000000000001, 282.6000000000008), (-134.63, 34.57, 139.0, 284.40000000000083), (-132.52, 38.5, 138.0, 286.20000000000084), (-113.18, 36.77, 119.0, 288.00000000000085), (-97.85, 35.23, 104.0, 289.80000000000086), (-92.05, 36.44, 99.0, 291.6000000000009), (-91.78, 39.71, 100.0, 293.4000000000009), (-92.29, 43.43, 102.0, 295.2000000000009), (-91.77, 46.76, 103.0, 297.0000000000009), (-91.14, 50.1, 104.0, 298.8000000000009), (-91.24, 53.96, 106.0, 300.60000000000093), (-91.19, 57.87, 108.0, 302.40000000000094), (-90.98, 61.83, 110.00000000000001, 304.20000000000095), (-90.61, 65.83, 112.00000000000001, 306.00000000000097), (-101.93, 79.07, 129.0, 307.800000000001), (-126.36, 104.54, 164.0, 309.600000000001), (-128.27, 113.08, 171.0, 311.400000000001), (-132.67, 124.59, 182.0, 313.200000000001), (-134.35, 134.35, 190.0, 315.000000000001), (-132.8, 141.42, 194.0, 316.80000000000103), (-123.67, 140.27, 187.0, 318.60000000000105), (-115.37, 139.46, 181.0, 320.40000000000106), (-107.87, 139.07, 176.0, 322.20000000000107), (-100.51, 138.34, 171.0, 324.0000000000011), (-93.31, 137.3, 166.0, 325.8000000000011), (-87.88, 138.47, 164.0, 327.6000000000011), (-86.54, 146.33, 170.0, 329.4000000000011), (-86.23, 156.86, 179.0, 331.2000000000011), (-90.8, 178.2, 200.0, 333.00000000000114), (-102.19, 217.16, 240.0, 334.80000000000115), (-100.48, 232.19, 252.99999999999997, 336.60000000000116), (-92.4, 233.37, 250.99999999999997, 338.40000000000117), (-84.35, 234.28, 249.00000000000003, 340.2000000000012), (-76.02, 233.96, 246.0, 342.0000000000012), (-67.79, 233.35, 243.00000000000003, 343.8000000000012), (-59.69, 232.46, 240.0, 345.6000000000012), (-51.92, 232.27, 238.0, 347.4000000000012), (-44.22, 231.82, 236.0, 349.20000000000124), (-36.61, 231.12, 234.0, 351.00000000000125), (-29.08, 230.17, 231.99999999999997, 352.80000000000126), (-21.74, 229.97, 231.0, 354.6000000000013), (-14.44, 229.55, 229.99999999999997, 356.4000000000013), (-7.19, 228.89, 229.0, 358.2000000000013), (0.0, 228.0, 227.99999999999997, 360.0000000000013), (-7.16, 227.89, 227.99999999999997, 358.2), (-14.32, 227.55, 227.99999999999997, 356.4), (-21.55, 227.98, 229.0, 354.59999999999997), (-28.7, 227.19, 229.0, 352.79999999999995), (-35.98, 227.17, 229.99999999999997, 350.99999999999994), (-43.29, 226.91, 231.0, 349.19999999999993), (-50.61, 226.41, 231.99999999999997, 347.3999999999999), (-58.19, 226.65, 234.0, 345.5999999999999), (-65.84, 226.63, 236.0, 343.7999999999999), (-73.55, 226.35, 238.0, 341.9999999999999), (-81.3, 225.81, 240.0, 340.1999999999999), (-89.45, 225.94, 243.00000000000003, 338.39999999999986), (-97.7, 225.77, 246.0, 336.59999999999985), (-106.02, 225.3, 249.00000000000003, 334.79999999999984), (-113.95, 223.64, 250.99999999999997, 332.99999999999983), (-122.85, 223.46, 254.99999999999997, 331.1999999999998), (-126.75, 214.32, 249.00000000000003, 329.3999999999998), (-108.77, 171.4, 202.99999999999997, 327.5999999999998), (-101.18, 148.87, 180.0, 325.7999999999998), (-100.51, 138.34, 171.0, 323.9999999999998), (-101.13, 130.38, 165.0, 322.19999999999976), (-105.17, 127.13, 165.0, 320.39999999999975), (-112.42, 127.52, 170.0, 318.59999999999974), (-119.8, 127.57, 175.0, 316.7999999999997), (-127.99, 127.99, 181.0, 314.9999999999997), (-136.32, 128.01, 187.0, 313.1999999999997), (-144.77, 127.63, 193.0, 311.3999999999997), (-148.71, 123.02, 193.0, 309.5999999999997), (-143.02, 110.94, 181.0, 307.79999999999967), (-138.34, 100.51, 171.0, 305.99999999999966), (-135.64, 92.18, 164.0, 304.19999999999965), (-114.83, 72.87, 136.0, 302.39999999999964), (-97.26, 57.52, 112.99999999999999, 300.5999999999996), (-96.39, 52.99, 110.00000000000001, 298.7999999999996), (-96.23, 49.03, 108.0, 296.9999999999996), (-95.91, 45.13, 106.0, 295.1999999999996), (-95.45, 41.3, 104.0, 293.3999999999996), (-95.77, 37.92, 103.0, 291.59999999999957), (-95.97, 34.55, 102.0, 289.79999999999956), (-95.11, 30.9, 100.0, 287.99999999999955), (-96.03, 27.9, 100.0, 286.19999999999953), (-99.76, 25.62, 103.0, 284.3999999999995), (-115.16, 25.74, 118.0, 282.5999999999995), (-135.56, 25.86, 138.0, 280.7999999999995), (-151.12, 23.93, 153.0, 278.9999999999995), (-151.79, 19.18, 153.0, 277.1999999999995), (-0.0, 0.0, 0.0, 275.39999999999947), (-0.0, 0.0, 0.0, 273.59999999999945), (-0.0, 0.0, 0.0, 271.79999999999944), (-0.0, -0.0, 0.0, 269.99999999999943), (-138.93, -4.37, 139.0, 268.1999999999994), (-130.74, -8.23, 131.0, 266.3999999999994), (-144.36, -13.65, 145.0, 264.5999999999994), (-146.83, -18.55, 148.0, 262.7999999999994), (-148.15, -23.47, 150.0, 260.9999999999994), (-151.27, -28.86, 154.0, 259.19999999999936), (-154.19, -34.47, 158.0, 257.39999999999935), (-154.0, -39.54, 159.0, 255.59999999999934), (-147.89, -42.96, 154.0, 253.79999999999933), (-131.25, -42.64, 138.0, 251.99999999999932), (-115.73, -41.66, 123.0, 250.1999999999993), (-102.28, -40.49, 110.00000000000001, 248.3999999999993), (-95.45, -41.3, 104.0, 246.59999999999928), (-93.2, -43.86, 103.0, 244.79999999999927), (-93.56, -47.67, 105.0, 242.99999999999926), (-93.76, -51.55, 107.0, 241.19999999999925), (-93.82, -55.49, 109.00000000000001, 239.39999999999924), (-93.72, -59.48, 111.00000000000001, 237.59999999999923), (-93.46, -63.52, 112.99999999999999, 235.79999999999922), (-93.04, -67.6, 114.99999999999999, 233.9999999999992), (-94.03, -72.94, 119.0, 232.1999999999992), (-97.86, -80.95, 127.0, 230.39999999999918), (-97.51, -85.97, 130.0, 228.59999999999917), (-94.77, -88.99, 130.0, 226.79999999999916), (-94.05, -94.05, 133.0, 224.99999999999915), (-94.47, -100.6, 138.0, 223.19999999999914), (-94.57, -107.27, 143.0, 221.39999999999912), (-94.34, -114.04, 148.0, 219.5999999999991), (-94.39, -121.68, 154.0, 217.7999999999991), (-94.63, -130.25, 161.0, 215.9999999999991), (-94.43, -138.95, 168.0, 214.19999999999908), (-93.77, -147.76, 175.0, 212.39999999999907), (-94.68, -160.1, 186.0, 210.59999999999906), (-94.42, -171.76, 196.0, 208.79999999999905), (-94.88, -186.22, 209.0, 206.99999999999903), (-94.52, -200.87, 222.00000000000003, 205.19999999999902), (-90.15, -208.33, 227.0, 203.399999999999), (-80.99, -204.55, 220.00000000000003, 201.599999999999), (-73.17, -203.23, 216.0, 199.799999999999), (-66.13, -203.53, 214.0, 197.99999999999898), (-58.87, -202.62, 211.0, 196.19999999999897), (-51.98, -202.43, 209.0, 194.39999999999895), (-45.16, -202.01, 206.99999999999997, 192.59999999999894), (-38.6, -202.35, 206.0, 190.79999999999893), (-31.91, -201.49, 204.0, 188.99999999999892), (-25.44, -201.4, 202.99999999999997, 187.1999999999989), (-19.01, -201.1, 202.0, 185.3999999999989), (-12.62, -200.6, 200.99999999999997, 183.5999999999989), (-6.31, -200.9, 200.99999999999997, 181.79999999999887), (0.0, -201.0, 200.99999999999997, 179.99999999999886), (6.34, -201.9, 202.0, 178.19999999999885), (12.81, -203.6, 204.0, 176.39999999999884), (18.35, -194.13, 195.0, 174.59999999999883), (18.67, -147.83, 149.0, 172.79999999999882), (22.21, -140.25, 142.0, 170.9999999999988), (26.42, -138.5, 141.0, 169.1999999999988), (30.98, -138.58, 142.0, 167.39999999999878), (37.8, -147.22, 152.0, 165.59999999999877), (46.59, -160.37, 167.0, 163.79999999999876), (58.1, -178.8, 188.0, 161.99999999999875), (67.07, -186.29, 198.0, 160.19999999999874), (49.33, -124.59, 134.0, 158.39999999999873), (47.26, -109.21, 119.0, 156.59999999999872), (51.09, -108.58, 120.0, 154.7999999999987), (56.29, -110.48, 124.0, 152.9999999999987), (64.55, -117.43, 134.0, 151.19999999999868), (73.81, -124.81, 145.0, 149.39999999999867), (78.77, -124.12, 147.0, 147.59999999999866), (93.31, -137.3, 166.0, 145.79999999999865), (135.19, -186.07, 229.99999999999997, 143.99999999999864), (155.68, -200.7, 254.0, 142.19999999999862), (165.73, -200.33, 260.0, 140.3999999999986), (175.91, -199.53, 266.0, 138.5999999999986), (185.51, -197.55, 271.0, 136.7999999999986), (189.5, -189.5, 268.0, 134.99999999999858), (169.12, -158.81, 231.99999999999997, 133.19999999999857), (168.02, -148.13, 224.00000000000003, 131.39999999999856), (132.53, -109.64, 172.0, 129.59999999999854), (239.42, -185.71, 303.0, 127.79999999999855), (246.75, -179.27, 305.0, 125.99999999999855), (243.16, -165.25, 294.0, 124.19999999999855), (260.9, -165.57, 309.0, 122.39999999999856), (281.46, -166.46, 327.0, 120.59999999999856), (263.77, -145.01, 301.0, 118.79999999999856), (238.79, -121.67, 268.0, 116.99999999999856), (257.88, -121.35, 285.0, 115.19999999999857), (263.4, -113.98, 287.0, 113.39999999999857), (278.93, -110.44, 300.0, 111.59999999999857), (280.38, -100.94, 298.0, 109.79999999999858), (261.54, -84.98, 275.0, 107.99999999999858), (218.95, -63.61, 227.99999999999997, 106.19999999999858), (193.72, -49.74, 200.0, 104.39999999999858), (181.52, -40.57, 186.0, 102.59999999999859), (181.72, -34.67, 185.0, 100.79999999999859), (181.73, -28.78, 184.0, 98.9999999999986), (181.56, -22.94, 183.0, 97.1999999999986), (181.19, -17.13, 182.0, 95.3999999999986), (180.64, -11.37, 181.0, 93.5999999999986), (180.91, -5.69, 181.0, 91.7999999999986), (181.0, 0.0, 181.0, 89.99999999999861), (180.91, 5.69, 181.0, 88.19999999999861), (180.64, 11.37, 181.0, 86.39999999999861), (181.19, 17.13, 182.0, 84.59999999999862), (180.56, 22.81, 182.0, 82.79999999999862), (180.75, 28.63, 183.0, 80.99999999999862), (180.74, 34.48, 184.0, 79.19999999999862), (180.54, 40.36, 185.0, 77.39999999999863), (172.41, 44.27, 178.0, 75.59999999999863), (144.04, 41.85, 150.0, 73.79999999999863), (120.78, 39.25, 127.0, 71.99999999999864), (111.02, 39.97, 118.0, 70.19999999999864), (109.71, 43.44, 118.0, 68.39999999999864), (109.21, 47.26, 119.0, 66.59999999999864), (109.48, 51.52, 121.0, 64.79999999999865), (108.7, 55.39, 122.0, 62.99999999999865), (109.54, 60.22, 125.0, 61.19999999999865), (109.31, 64.65, 127.0, 59.399999999998656), (109.76, 69.66, 130.0, 57.59999999999866), (121.58, 82.63, 147.0, 55.79999999999866), (149.67, 108.74, 185.0, 53.999999999998664), (145.39, 112.77, 184.0, 52.19999999999867), (135.61, 112.19, 176.0, 50.39999999999867), (126.77, 111.76, 169.0, 48.59999999999867), (118.09, 110.9, 162.0, 46.799999999998676), (115.26, 115.26, 163.0, 44.99999999999868), (114.32, 121.74, 167.0, 43.19999999999868), (115.07, 130.52, 174.0, 41.399999999998684), (115.37, 139.46, 181.0, 39.59999999999869), (114.61, 147.76, 187.0, 37.79999999999869), (115.21, 158.57, 196.0, 35.99999999999869), (115.79, 170.38, 206.0, 34.199999999998695), (115.2, 181.53, 215.0, 32.3999999999987), (117.59, 198.83, 231.0, 30.599999999998698), (121.88, 221.71, 252.99999999999997, 28.799999999998697), (117.13, 229.88, 258.0, 26.999999999998696), (107.72, 228.92, 252.99999999999997, 25.199999999998695), (100.88, 233.11, 254.0, 23.399999999998695), (91.66, 231.51, 249.00000000000003, 21.599999999998694), (83.33, 231.46, 246.0, 19.799999999998693), (75.09, 231.11, 243.00000000000003, 17.999999999998693), (66.96, 230.47, 240.0, 16.199999999998692), (59.19, 230.52, 238.0, 14.399999999998691), (51.48, 230.32, 236.0, 12.59999999999869), (43.85, 229.86, 234.0, 10.79999999999869), (36.29, 229.14, 231.99999999999997, 8.999999999998689), (28.95, 229.18, 231.0, 7.199999999998689), (21.64, 228.98, 229.99999999999997, 5.399999999998689), (14.38, 228.55, 229.0, 3.5999999999986896), (7.16, 227.89, 227.99999999999997, 1.7999999999986895), (-0.0, 228.0, 227.99999999999997, -1.3105072582675348e-12), (6.6, 229.9), (13.12, 228.59), (19.67, 228.07), (26.19, 227.35), (32.85, 227.41), (39.54, 227.26), (46.25, 226.89), (52.97, 226.31), (59.7, 225.5), (66.44, 224.48), (73.51, 224.17), (80.62, 223.62), (88.17, 223.74), (95.37, 222.68), (103.51, 223.15), (111.29, 222.43), (119.62, 222.27), (126.46, 219.26), (134.9, 218.5), (138.72, 210.93), (147.71, 210.43), (137.68, 186.43), (134.25, 172.27), (132.12, 160.69), (131.52, 151.52), (130.49, 142.53), (129.02, 133.75), (127.91, 125.81), (127.21, 118.68), (126.21, 111.69), (126.54, 106.0), (127.49, 100.91), (134.28, 99.41), (142.84, 98.53), (153.25, 98.09), (163.77, 97.07), (166.11, 91.88), (151.55, 80.0), (115.73, 61.66), (115.08, 57.39), (114.27, 53.2), (113.32, 49.1), (113.21, 45.3), (112.96, 41.55), (112.6, 37.83), (112.11, 34.16), (114.49, 30.82), (128.75, 28.1), (166.92, 25.25), (183.0, 20.0), (181.91, 14.280000000000001), (181.64, 8.57), (181.19, 2.870000000000001), (180.56, -2.8099999999999987), (179.76, -8.469999999999999), (178.78, -14.100000000000001), (178.59, -19.92), (177.25, -25.509999999999998), (176.69, -31.33), (176.9, -37.48), (175.94, -43.34), (175.73, -49.58), (175.29, -55.86), (179.16, -64.3), (198.69, -81.24), (240.98, -112.47999999999999), (265.11, -136.78), (260.9, -145.57), (243.16, -145.25), (245.13, -158.1), (0.0, 20.0), (248.11, -185.25), (246.04, -196.91), (221.61, -188.1), (218.5, -198.5), (222.48, -216.91), (208.31, -216.28), (177.2, -194.2), (127.48, -144.35), (158.7, -198.43), (160.76, -216.55), (150.03, -216.41), (139.48, -215.84), (129.11, -214.85), (116.22, -208.1), (91.54, -174.54), (68.71, -138.77), (65.16, -144.57), (56.57, -137.13), (46.66, -123.61000000000001), (38.78, -113.47999999999999), (34.32, -113.66), (31.85, -122.47999999999999), (34.1, -158.78), (30.04, -169.64), (22.43, -157.59), (15.72, -146.26), (9.98, -138.69), (5.03, -139.92), (-0.0, -159.0), (-6.88, -198.89), (-14.0, -202.56), (-20.7, -199.02), (-27.57, -198.27), (-34.42, -197.29), (-41.41, -197.09), (-48.21, -195.68), (-55.21, -195.03), (-62.49, -195.11), (-69.53, -193.99), (-76.89, -193.58), (-84.67, -193.85), (-92.14, -192.92), (-100.06, -192.63), (-108.96, -193.84), (-117.07, -192.94), (-117.59, -178.83), (-115.74, -162.37), (-114.1, -147.9), (-112.27, -134.52), (-110.94, -123.02000000000001), (-110.27, -113.30000000000001), (-109.12, -103.77), (-108.16, -95.18), (-106.77, -86.77), (-106.43, -79.94), (-106.52, -73.91), (-107.87, -69.24), (-103.51, -60.290000000000006), (-101.94, -54.06), (-101.73, -49.14), (-101.32, -44.3), (-100.71, -39.56), (-99.9, -34.92), (-99.79, -30.85), (-101.34, -27.689999999999998), (-108.3, -26.86), (-117.15, -26.380000000000003), (-127.96, -26.07), (-140.76, -25.729999999999997), (-153.65, -24.64), (-159.82, -21.03), (-159.07, -15.560000000000002), (-155.2, -9.61), (-153.09, -4.25), (-150.8, 0.9499999999999993), (-140.37, 6.73), (-138.73, 11.27), (-151.92, 15.23), (-152.0, 20.0), (-151.92, 24.77), (-137.73, 28.67), (-83.63, 27.91), (-39.68, 25.009999999999998), (-37.53, 25.94), (-63.85, 32.18), (-94.66, 41.16), (-92.98, 43.870000000000005), (-92.19, 46.78), (-92.25, 49.97), (-92.21, 53.2), (-92.05, 56.44), (-91.78, 59.71), (-91.39, 63.0), (-90.88, 66.31), (-91.14, 70.1), (-103.29, 81.08), (-119.05, 95.55), (-130.68, 108.81), (-128.63, 113.46), (-130.38, 121.13), (-137.15, 133.45999999999998), (-138.77, 142.34), (-132.67, 144.59), (-123.04, 143.04000000000002), (-114.32, 141.74), (-107.13, 141.51999999999998), (-99.44, 140.2), (-92.55, 139.31), (-88.17, 141.35), (-86.0, 146.54000000000002), (-85.73, 155.09), (-85.52, 164.6), (-96.35, 195.26), (-108.05, 232.06), (-101.34, 235.35), (-92.54, 233.84), (-86.14, 237.57), (-77.91, 236.4), (-70.15, 235.89), (-62.49, 235.11), (-54.96, 234.06), (-47.77, 233.73), (-40.66, 233.16), (-33.63, 232.35), (-26.7, 231.32), (-19.95, 231.06), (-13.25, 230.58), (-6.63, 230.9), (0.0, 230.0), (-6.6, 229.9), (-13.19, 229.59), (-19.76, 229.07), (-26.45, 229.34), (-33.16, 229.39), (-39.72, 228.24), (-46.68, 228.85), (-53.47, 228.25), (-60.54, 228.38), (-67.67, 228.28), (-74.86, 227.93), (-82.46, 228.27), (-90.15, 228.33), (-97.93, 228.11), (-105.78, 227.6), (-113.21, 225.93), (-121.15, 224.86), (-128.6, 222.64), (-115.79, 190.38), (-98.75, 155.91), (-98.68, 147.20999999999998), (-98.16, 138.66), (-99.2, 132.51999999999998), (-103.37, 130.07), (-110.31, 130.31), (-117.36, 130.20999999999998), (-125.27, 130.44), (-134.07, 130.91), (-143.02, 130.94), (-149.67, 128.74), (-148.05, 120.61), (-141.0, 109.48), (-137.72, 101.45), (-138.46, 96.12), (-129.2, 85.83), (-106.77, 70.24000000000001), (-94.53, 60.91), (-94.84, 57.55), (-95.03, 54.21), (-95.11, 50.9), (-95.07, 47.620000000000005), (-94.92, 44.370000000000005), (-93.69, 40.94), (-95.28, 38.18), (-96.79, 35.33), (-95.24, 32.03), (-0.0, 20.0), (-0.0, 20.0), (-0.0, 20.0), (-0.0, 20.0), (-154.92, 15.129999999999999), (-153.7, 10.33), (-154.31, 5.41), (-152.79, 0.6999999999999993), (-144.2, -2.84), (-134.57, -5.670000000000002), (-148.34, -13.159999999999997), (-151.1, -18.799999999999997), (-151.73, -24.08), (-154.07, -30.060000000000002), (-155.25, -35.89), (-150.62, -39.64), (-137.66, -39.57), (-124.87, -38.76), (-114.05, -38.11), (-104.28, -37.33), (-97.26, -37.52), (-94.56, -40.01), (-94.29, -44.08), (-93.85, -48.18000000000001), (-94.03, -52.94), (-94.77, -58.400000000000006), (-94.51, -63.33), (-94.04, -68.31), (-97.58, -77.58), (-97.21, -83.51), (-95.89, -88.77), (-95.61, -95.58), (-95.61, -103.26), (-95.81, -111.87), (-96.12, -121.43), (-95.91, -131.13), (-96.21, -142.68), (-96.35, -155.26), (-96.7, -169.78), (-97.08, -186.3), (-95.32, -200.26), (-89.09, -205.01), (-79.94, -202.05), (-71.69, -200.65), (-64.17, -200.87), (-56.7, -200.84), (-49.3, -200.56), (-41.97, -200.03), (-34.88, -200.25), (-27.82, -200.25), (-20.8, -200.02), (-13.81, -199.57), (-6.91, -199.89), (0.0, -200.0), (6.97, -201.89), (13.94, -201.56), (17.97, -170.15), (20.05, -138.74), (24.87, -137.04), (30.36, -139.13), (39.05, -154.69), (47.0, -163.06), (53.01, -162.46), (49.44, -132.17), (46.41, -108.9), (51.17, -109.24000000000001), (59.18, -116.75), (71.53, -132.01), (79.45, -135.93), (90.09, -143.87), (95.7, -141.82), (136.64, -195.3), (149.51, -200.0), (159.88, -200.05), (170.39, -199.66), (180.39, -198.06), (185.83, -190.78), (173.19, -164.43), (129.4, -109.4), (225.25, -191.53), (239.29, -190.96), (246.56, -183.98), (240.21, -166.32), (254.03, -164.56), (277.07, -168.3), (260.9, -145.57), (234.12, -118.46000000000001), (270.78, -128.86), (0.0, 20.0), (278.69, -111.13999999999999), (270.74, -97.16), (220.36, -67.25), (186.29, -47.06999999999999), (182.6, -39.33), (182.46, -33.01), (182.09, -26.75), (181.52, -20.57), (181.72, -14.670000000000002), (181.73, -8.780000000000001), (181.56, -2.9400000000000013), (181.19, 2.870000000000001), (181.64, 8.57), (181.91, 14.280000000000001), (182.0, 20.0), (181.91, 25.72), (181.64, 31.43), (181.19, 37.129999999999995), (174.61, 42.06), (138.28, 41.9), (111.98, 41.36), (110.28, 44.65), (110.42, 48.35), (110.43, 52.08), (110.32, 55.85), (110.08, 59.63), (109.71, 63.44), (110.13, 67.66), (110.39, 71.95), (123.85, 83.1), (163.87, 110.09), (158.38, 113.66), (146.91, 113.23), (136.47, 112.74), (127.82, 112.87), (120.89, 113.77), (116.35, 116.25), (116.27, 122.5), (115.91, 128.84), (116.67, 136.67000000000002), (116.37, 143.92000000000002), (117.05, 152.77), (116.65, 161.0), (117.07, 170.92), (117.56, 181.8), (118.6, 194.51), (124.31, 215.88), (124.72, 230.88), (114.18, 227.68), (108.5, 232.95), (100.06, 232.63), (92.14, 232.92), (83.93, 231.99), (76.22, 231.7), (68.6, 231.13), (61.38, 231.26), (54.21, 231.15), (47.12, 230.8), (40.1, 230.21), (33.32, 230.38), (26.57, 230.33), (19.86, 230.06), (13.19, 229.59), (6.6, 229.9), (-0.0, 229.0)]

x = [x[0]for x in env_map if x[0] > -800 and x[0] < 800]
y = [y[1]for y in env_map if y[0] > -800 and y[0] < 800]

plt.scatter(x, y)
plt.show()
