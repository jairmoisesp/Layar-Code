# Layar-Code
Layar is a script developed in Python that calculates the area of all mask of a layout.

STEPS:
1. Select the .GDS file of the layout
2. Download OwlVision Viewer, this software will help us in: Visualize the layout and convert the .GDS file into a ASCII format
3. Open the .GDS file in the OwlVision and Translate it to ASCII format
4. Edit line 20 of Layar Code with the name of the ASCII file.
5. Compile

Layar has as output:
- All the mask available in the layout and all box area found.
![image](https://user-images.githubusercontent.com/110146406/181416824-96266bc4-df59-437a-9d09-cb5541662780.png)

- Data (Width, Large and Area) of each box area
![image](https://user-images.githubusercontent.com/110146406/181416903-30823d0f-d669-4148-88af-2f455a2ac8c0.png)

- Data (Large and Area) of the polysilicon used in the layouts
- ![image](https://user-images.githubusercontent.com/110146406/181416947-0470d587-60e9-4857-8521-68657fce88fb.png)

Note: The Poly mask has to be assigned to LAYER 2 during the layout generation process. Otherwise, change line 92 with the corresponding Layer name for the poly mask
