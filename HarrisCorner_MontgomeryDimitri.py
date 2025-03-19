# Dimitri Montgomery
# Harris Corner Detection


import numpy as np
import cv2


def Imatrices(emptyIMGIx, emptyIMGIy, emptyIMGIxx, emptyIMGIyy, emptyIMGIxy):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Calculate x gradient using horizontal neighbors
            emptyIMGIx[i, j] = float(image[i, j + 1]) - float(image[i, j - 1])

            # Calculate y gradient using vertical neighbors
            emptyIMGIy[i, j] = float(image[i + 1, j]) - float(image[i - 1, j])

            # Calculate products of gradients
            emptyIMGIxx[i, j] = emptyIMGIx[i, j] * emptyIMGIx[i, j]
            emptyIMGIyy[i][j] = emptyIMGIy[i, j] * emptyIMGIy[i, j]
            emptyIMGIxy[i][j] = emptyIMGIx[i, j] * emptyIMGIy[i, j]

    return emptyIMGIx, emptyIMGIy, emptyIMGIxx, emptyIMGIyy, emptyIMGIxy


def fillCornerMTX(emptyIMGIxx, emptyIMGIyy, emptyIMGIxy):
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):

            # Initialize sums for 3x3 window
            sumIxx = 0
            sumIyy = 0
            sumIxy = 0

            # Define window boundaries
            startI = i - 1
            endI = i + 2
            startJ = j - 1
            endJ = j + 2

            # Sum gradient values in the window
            for x in range(startI, endI):
                for y in range(startJ, endJ):
                    sumIxx += emptyIMGIxx[x, y]
                    sumIyy += emptyIMGIyy[x, y]
                    sumIxy += emptyIMGIxy[x, y]

            # Calculate cornerness using Harris formula
            det_M = (sumIxx * sumIyy) - (sumIxy * sumIxy)
            trace_M = (sumIxx + sumIyy)
            c = (det_M) - 0.05 * (trace_M**2)
            #c = (sumIxx) * (sumIyy) - ((sumIxy) ** 2) - 0.05 * ((sumIxx + sumIyy) ** 2)

            emptyCornerIMG[i, j] = c

    return emptyCornerIMG


def viewCornersMethod1(emptyCornerIMGFilled, finalCornerIMG):
    rows = emptyCornerIMGFilled.shape[0]
    cols = emptyCornerIMGFilled.shape[1]

    # Collect all cornerness values
    store_vals = []
    for i in range(rows):
        for j in range(cols):
            store_vals.append(emptyCornerIMGFilled[i, j])

    # Find maximum cornerness value
    max_val = max(store_vals)

    # Set threshold as percentage of max value
    valid_c = max_val * 0.1

    # Mark corners above threshold
    for i in range(rows):
        for j in range(cols):
            if emptyCornerIMGFilled[i, j] >= valid_c:
                cv2.circle(finalCornerIMG, (j, i), 3, (0, 255, 0), -1)

    return finalCornerIMG





def viewCornersMethod2(emptyCornerIMGFilled, finalCornerIMG):
    rows = emptyCornerIMGFilled.shape[0]
    cols = emptyCornerIMGFilled.shape[1]

    # Find global max for global threshold
    store_vals = []
    for i in range(rows):
        for j in range(cols):
            store_vals.append(emptyCornerIMGFilled[i, j])

    max_val = max(store_vals)
    threshold = max_val * 0.05

    # Block size for dividing the image
    block_size = 10

    # Process each block
    for i in range(block_size, rows - block_size, block_size):
        for j in range(block_size, cols - block_size, block_size):
            # get current block window
            block_window = emptyCornerIMGFilled[i - block_size:i + block_size, j - block_size:j + block_size]

            # Find maximum value in this block
            store_vals = []
            for x in range(block_window.shape[0]):
                for y in range(block_window.shape[1]):
                    store_vals.append(block_window[x, y])

            block_max = max(store_vals)

            # Only process blocks with significant cornerness values
            if block_max > threshold:
                # Find position of maximum value in block
                max_val = 0
                max_i, max_j = 0, 0
                for a in range(block_window.shape[0]):
                    for b in range(block_window.shape[1]):
                        if block_window[a, b] > max_val:
                            max_val = block_window[a, b]
                            max_i, max_j = a, b

                # Convert block coordinates to image coordinates
                block_i = i - block_size + max_i
                block_j = j - block_size + max_j

                # Mark corner
                cv2.circle(finalCornerIMG, (block_j, block_i), 3, (0, 255, 0), -1)

    return finalCornerIMG


if __name__ == "__main__":

    print("What type of image would you like to display\n1. Checker board\n2. High contrast mushroom\n3. City scape\n4. Landscape\n5. Low contrast dog\n6. Person\n7. View your own image\n8. Exit")
    user_choice = int(input("Enter you choice(1-6): "))
    if user_choice == 1:
        image = cv2.imread("checkerboard.png", 0)
        finalCornerIMG = cv2.imread("checkerboard.png")
    elif user_choice == 2:
        image = cv2.imread("red-mushroom.png", 0)
        finalCornerIMG = cv2.imread("red-mushroom.png")
    elif user_choice == 3:
        image = cv2.imread("Architecture-PNG-Photo-Image.png", 0)
        finalCornerIMG = cv2.imread("Architecture-PNG-Photo-Image.png")
    elif user_choice == 4:
        image = cv2.imread("landscape.jpg", 0)
        finalCornerIMG = cv2.imread("landscape.jpg")
    elif user_choice == 5:
        image = cv2.imread("low contrast.png", 0)
        finalCornerIMG = cv2.imread("low contrast.png")
    elif user_choice == 6:
        image = cv2.imread("person2.png", 0)
        finalCornerIMG = cv2.imread("person2.png")
    elif user_choice == 7:
        user_file = str(input("Enter your image name, be sure to add .png, .jpeg, .pdf, etc at the end of the file name: "))
        image = cv2.imread(user_file, 0)
        finalCornerIMG = cv2.imread(user_file)
    else:
        print("Invalid choice rerun program and choose again")

    rows = image.shape[0]
    cols = image.shape[1]


    # Create empty images for Ix, Iy, Ixx, Iyy, and Ixy (all the same dimensions as your original image)
    emptyIMGIx = np.zeros((rows, cols), np.float32)
    emptyIMGIy = np.zeros((rows, cols), np.float32)
    emptyIMGIxx = np.zeros((rows, cols), np.float32)
    emptyIMGIyy = np.zeros((rows, cols), np.float32)
    emptyIMGIxy = np.zeros((rows, cols), np.float32)
    emptyCornerIMG = np.zeros((rows, cols), np.float32)


    # Calculate gradients and their values
    emptyIMGIx, emptyIMGIy, emptyIMGIxx, emptyIMGIyy, emptyIMGIxy = Imatrices(emptyIMGIx, emptyIMGIy, emptyIMGIxx, emptyIMGIyy, emptyIMGIxy)

    # Display gradient stats
    print("\nGradient stats: ")
    print(f"Max Ix: {np.max(emptyIMGIx)}, Min Ix: {np.min(emptyIMGIx)}")
    print(f"Max Iy: {np.max(emptyIMGIy)}, Min Iy: {np.min(emptyIMGIy)}")
    print(f"Max Ixx: {np.max(emptyIMGIxx)}, Min Ixx: {np.min(emptyIMGIxx)}")
    print(f"Max IYY: {np.max(emptyIMGIyy)}, Min Iyy: {np.min(emptyIMGIyy)}")
    print(f"Max Ixy: {np.max(emptyIMGIxy)}, Min Ixy: {np.min(emptyIMGIxy)}")

    # Calculate cornerness values
    emptyCornerIMGFilled = fillCornerMTX(emptyIMGIxx, emptyIMGIyy, emptyIMGIxy)

    # User menu for selecting detection method
    print("1. Method 1: basic method\n2. Method 2: break image into blocks and compute\n3. Exit")
    user_input = int(input("Enter which method to use to calculate and view Harris Corner values(1-3): "))


    # Process based on user selection
    if user_input == 1:
        # Apply Method 1 (global threshold)
        harrisCornerIMG = viewCornersMethod1(emptyCornerIMGFilled, finalCornerIMG)
        cv2.imshow("Harris_Corner_Detection", harrisCornerIMG / 255.0)
        cv2.imwrite("assign3_HarrisCorner_Detection.png", harrisCornerIMG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif user_input == 2:
        # Apply Method 2 (block-based threshold)
        harrisCornerIMG = viewCornersMethod2(emptyCornerIMGFilled, finalCornerIMG)
        cv2.imshow("Harris_Corner_Detection", harrisCornerIMG / 255.0)
        cv2.imwrite("assign3_HarrisCorner_Detection.png", harrisCornerIMG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Exiting program")

















