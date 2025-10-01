from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

# Biến toàn cục
angle_h = 0.0
angle_v = 0.0
radius = 30.0 #Tầm nhìn Camera
mouse_down = False
last_x = 0
last_y = 0
show_paper = True
light_on = True

def init():
    glClearColor(0.1, 0.1, 0.3, 1.0)  # Nền pastel

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    light_pos = [10.0, 12.0, 10.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    # Ánh sáng hơi ngả vàng
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 0.925, 1.0])     # Vàng nhạt
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 0.9, 1.0])    # Phản chiếu ánh sáng vàng


    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.6, 0.6, 0.6, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [80.0])

    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Hàm xử lý sự kiện chuột
def mouse(button, state, x, y):
    global mouse_down, last_x, last_y
    if button == GLUT_LEFT_BUTTON:
        mouse_down = (state == GLUT_DOWN)
        last_x, last_y = x, y
# Hàm xử lý chuyển động chuột
def motion(x, y):
    global last_x, last_y, angle_h, angle_v
    if mouse_down:
        angle_h += (x - last_x) * 0.5 # Cập nhật góc ngang
        angle_v = max(-89, min(89, angle_v - (y - last_y) * 0.5)) # Cập nhật góc dọc
        last_x, last_y = x, y
        glutPostRedisplay()

#==================================
#-------------Sàn nhà--------------
#==================================

def draw_floor():
    floor_color = ((0.4863, 0.4863, 0.4863))  # Màu xanh pastel sáng
    draw_box(0, -1.5, 0, 20.0, 1.5, 25.0, color=floor_color) #Độ dài rộng vị trí
    
    #Sàn nhà gỗ
    draw_box(-0.4, 0, 0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, 2.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, 4.0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, 6.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, 8.0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, 10.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, 11.4, 19.2, 0.15, 0.8, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, 0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, -2.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, -4.0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, -6.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, -8.0, 19.2, 0.15, 2.0, color=(1.0, 0.7725, 0.3137))
    draw_box(-0.4, 0, -10.0, 19.2, 0.15, 2.0, color=(1.0, 0.7961, 0.3922))
    draw_box(-0.4, 0, -11.7, 19.2, 0.15, 1.6, color=(1.0, 0.7725, 0.3137))
    

def draw_box(x, y, z, w, h, d, color=(0.4, 0.86, 1.0)):
    glColor3f(*color)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [*color, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100.0)

    glPushMatrix()
    glTranslatef(x, y + h / 2.0, z)
    glScalef(w, h, d)
    glutSolidCube(1.0)
    glPopMatrix()
#==================================
#---------------End----------------
#==================================    
    
#==================================
#-------------Tường----------------
#==================================
def draw_wall():
    #Không gian phòng học
    # Tường phía sau
    draw_box(0, 0.5, 12.1, 20.0, 9.5, 0.8, color=(0.7843, 0.7882, 0.6510))
    # Effec 1
    draw_box(-0.4, 0.15, 11.7, 19.2, 0.35, 0.1, color=(0.4, 0.4, 0.4))
    #Màu tường
    draw_box(-0.4, 0.5, 11.7, 19.2, 9.5, 0.1, color=(0.686, 0.0, 0.0))
    # Tường phía sau 2
    draw_box(0, 0, 12.1, 20.0, 0.5, 0.8, color=(0.6078, 0.6078, 0.6078))
    # Tường phía sau 3
    draw_box(0, 10.0, 12.1, 20.0, 0.5, 0.8, color=(1.0, 1.0, 1.0))
    # Tường bên trái1
    draw_box(9.60, 2.0, 10.0, 0.8, 6.0, 5.0, color=(0.7843, 0.7882, 0.6510))
    # Tường bên trái2
    draw_box(9.60, 2.0, 0, 0.8, 6.0, 5.0, color=(0.7843, 0.7882, 0.6510))
    # Tường bên trái3
    draw_box(9.60, 2.0, -10.0, 0.8, 6.0, 5.0, color=(0.7843, 0.7882, 0.6510))
    # Tường dưới
    draw_box(9.60, 0.5, 0, 0.8, 1.5, 25.0, color=(0.7843, 0.7882, 0.6510))
    # Tường dưới 2
    draw_box(9.60, 0, 0, 0.8, 0.5, 25.0, color=(0.6078, 0.6078, 0.6078))
    # Effec 2
    draw_box(9.2, 0.15, -0.4, 0.1, 0.35, 24.2, color=(0.4, 0.4, 0.4))
    # Tường trên
    draw_box(9.60, 8.0, 0, 0.8, 2.0, 25.0, color=(0.7843, 0.7882, 0.6510))
    # Tường trên 2
    draw_box(9.60, 10.0, 0, 0.8, 0.5, 25.0, color=(1.0, 1.0, 1.0))
    # Hết
    
    #Cửa sổ
    # Khung cửa sổ
    draw_box(9.80, 2.0, 5.0, 0.2, 0.2, 5.0, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 2
    draw_box(9.80, 2.0, -5.0, 0.2, 0.2, 5.0, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 3
    draw_box(9.80, 7.8, -5.0, 0.2, 0.2, 5.0, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 4
    draw_box(9.80, 7.8, 5.0, 0.2, 0.2, 5.0, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 7
    draw_box(9.80, 2.0, -7.5, 0.2, 6.0, 0.2, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 8
    draw_box(9.80, 2.0, 7.5, 0.2, 6.0, 0.2, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 9
    draw_box(9.80, 2.0, -2.5, 0.2, 6.0, 0.2, color=(1.0, 1.0, 1.0))
    # Khung cửa sổ 10
    draw_box(9.80, 2.0, 2.5, 0.2, 6.0, 0.2, color=(1.0, 1.0, 1.0))
    #Hết
    
    #Cửa sổ kéo
    # Khung cửa sổ kéo 1
    draw_box(9.80, 6.0, -5.0, 0.15, 0.1, 5.0, color=(0.9098, 0.6667, 0.2392))
    # Khung cửa sổ kéo 2
    draw_box(9.80, 6.0, 5.0, 0.15, 0.1, 5.0, color=(0.9098, 0.6667, 0.2392))
    # Cửa sổ kéo 1
    draw_box(9.80, 6.1, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.2, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.3, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.4, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.5, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.6, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.7, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.8, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.9, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.0, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.1, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.2, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.3, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.4, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.5, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.6, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.7, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.8, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.9, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 8.0, 5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    # Cửa sổ kéo 2
    draw_box(9.80, 6.1, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.2, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.3, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.4, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.5, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.6, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.7, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.8, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 6.9, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.0, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.1, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.2, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.3, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.4, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.5, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.6, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.7, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.8, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 7.9, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))
    draw_box(9.80, 8.0, -5.0, 0.15, 0.05, 5.0, color=(0.9922, 1.0, 0.8824))


def draw_paint():
    #Tranh treo tường
    # tranh 1
    draw_box(9.2, 5.6, 0, 0.1, 2.5, 2.0, color=(0.211, 0.211, 0.211))
    draw_box(9.1, 5.7, 0, 0.01, 2.3, 1.8, color=(1.0, 1.0, 1.0))
    draw_box(9.09, 6.2, 0, 0.01, 1.5, 1.0, color=(0.8, 0.1, 0.1))

#==================================
#---------------End----------------
#==================================


#==================================
#----------Bàn giáo viên-----------
#==================================

#Bàn giáo viên
def draw_table_teacher(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
        
    #Kích thước mặt bàn 1
    table_width = 5.0
    table_depth = 3.0
    table_thickness = 0.2 #Độ dày mặt bàn
    table_height = 2.7 #Chiều cao từ mặt sàn tới bàn
    #Mặt bàn 2
    table_width_front = 5.0
    table_depth_front = 3.0
    table_thickness_front = 0.1
    table_height_front = 2.7
    #Mặt bàn 3
    table_width_front_3 = 4.9
    table_depth_front_3 = 3.0
    table_thickness_front_3 = 0.1
    table_height_front_3 = 1.8
    
    
    
    #Mặt bàn 1
    table_color = (1.0, 0.978, 0.9) #Chỉnh màu bàn
    draw_box(x_offset, table_height, z_offset, table_width, table_thickness, table_depth, table_color)
    
    #Mặt bàn 2
    table_color = (1.0, 0.9, 0.5)
    draw_box(x_offset, table_height_front, z_offset, table_width_front, table_thickness_front, table_depth_front, table_color)
    
   
    
    #Mặt bàn 3
    table_color = (1.0, 0.8588, 0.4627)
    draw_box(x_offset, table_height_front_3, z_offset, table_width_front_3, table_thickness_front_3, table_depth_front_3, table_color)
    
    #Kích thước chân bàn
    leg_w, leg_d, leg_h = 0.1, 0.1, table_height
    dx = table_width / 2 - leg_w / 2 #Khoảng cách từ tâm bàn đến rìa ngoài của bàn theo chiều ngang
    dz = table_depth / 2- leg_d / 2 #Khoảng cách từ tâm bàn đến rìa ngoài của bàn theo chiều sâu
    
    #Vị trí 4 chân bàn sát với mép bàn
    leg_color = (1.0, 0.978, 0.9)
    floor_y = -0.1
    draw_box(x_offset - dx, floor_y + leg_h / 10, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, floor_y + leg_h / 10, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset - dx, floor_y + leg_h / 10, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, floor_y + leg_h / 10, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)
    
    #Ngăn dưới 1
    box_w, box_d, box_h = 5.0, 0.1, 3.3
    
    #Vị trí ngăn bàn
    box_color = (0.361, 0.380, 0.467)
    draw_box(x_offset, 0, 5.5, box_w, box_h, box_d, color=box_color)
    draw_box(x_offset, 0, 5.6, box_w, box_h, 0.05, color=(0.918, 0.565, 0.0))
    draw_box(6.5, 0, 7.0, 0.1, 4.0, 3.0, color=box_color)
    draw_box(6.4, 0, 7.0, 0.1, 4.0, 3.0, color=(0.918, 0.565, 0.0))
    draw_box(1.5, 0, 7.0, 0.1, 3.0, 3.0, color=box_color)
    draw_box(1.6, 0, 7.0, 0.1, 3.0, 3.0, color=(0.918, 0.565, 0.0))

#Tài liệu
def draw_folder():
    draw_box(6.0, 2.9, 6.5, 0.5, 1.3, 1.6, color=(0.95, 0.95, 0.95))
    draw_box(6.25, 2.9, 6.5, 0.01, 1.3, 1.6, color=(0.333, 0.431, 0.897))
    draw_box(5.75, 2.9, 6.5, 0.01, 1.3, 1.6, color=(0.333, 0.431, 0.897))
    draw_box(6.0, 2.9, 5.7, 0.5, 1.3, 0.01, color=(0.333, 0.431, 0.897))
    draw_box(6.0, 2.9, 5.69, 0.35, 0.7, 0.01, color=(0.875, 0.875, 0.875))
    draw_box(6.0, 3.8, 5.69, 0.35, 0.1, 0.01, color=(0.875, 0.875, 0.875))
    draw_box(6.0, 4.0, 5.69, 0.35, 0.05, 0.01, color=(0.875, 0.875, 0.875))
    
    #Sách phụ kiện
    draw_box(5.7, 2.9, 6.2, 0.1, 0.8, 0.5, color=(0.95, 0.13, 0.23))
    draw_box(5.6, 2.9, 6.2, 0.1, 0.7, 0.55, color=(0.0, 0.59, 0.95))
    draw_box(5.5, 2.9, 6.2, 0.1, 0.6, 0.55, color=(0.58, 0.59, 0.95))
    draw_box(5.4, 2.9, 6.2, 0.1, 0.65, 0.5, color=(0.78, 0.23, 0.95))
    draw_box(5.3, 2.9, 6.2, 0.1, 0.75, 0.55, color=(0.78, 0.95, 0.23))
    

def draw_PC():    
    #Case máy tính
    draw_box(7.2, 2.0, 7.0, 1.0, 0.1, 1.6, color=(0.13, 0.15, 0.134))
    draw_box(7.2, 0, 7.0, 1.0, 2.0, 1.5, color=(0.2, 0.2, 0.28))
    draw_box(7.2, 0.3, 7.0, 0.6, 0.4, 1.6, color=(0.43, 0.42, 0.47))
    draw_box(7.2, 0.8, 7.0, 0.6, 0.2, 1.6, color=(0.43, 0.42, 0.632))
    draw_box(7.2, 1.8, 7.0, 0.6, 0.2, 1.6, color=(0.13, 0.15, 0.134))
    draw_box(7.2, 1.6, 7.0, 0.1, 0.1, 1.6, color=(0.271, 1.0, 0.251))
    draw_box(7.0, 1.6, 7.0, 0.1, 0.1, 1.6, color=(1.0, 0.263, 0.263))
    
    #Chuột máy tính
    draw_box(5.4, 2.9, 7.5, 0.3, 0.2, 0.5, color=(0.13, 0.15, 0.134))
    draw_box(5.4, 2.91, 7.4, 0.05, 0.21, 0.1, color=(0.423, 0.423, 0.423))
    
    #PC
    draw_box(4.0, 2.9, 6.5, 0.7, 0.1, 0.4, color=(0.13, 0.15, 0.134))
    draw_box(4.0, 2.92, 6.5, 0.2, 0.8, 0.06, color=(0.423, 0.423, 0.423))
    draw_box(4.0, 3.6, 6.5, 0.3, 0.3, 0.15, color=(0.13, 0.15, 0.134))
    draw_box(4.0, 3.2, 6.6, 2.0, 1.3, 0.08, color=(0.223, 0.223, 0.223))
    
    #Bàn phím
    draw_box(4.0, 2.9, 7.7, 1.4, 0.05, 0.5, color=(0.13, 0.15, 0.134))
    draw_box(3.83, 2.91, 7.777, 1.0, 0.05, 0.3, color=(0.423, 0.423, 0.423))
    draw_box(3.83, 2.91, 7.533, 1.0, 0.05, 0.1, color=(0.423, 0.423, 0.423))
    draw_box(4.53, 2.91, 7.777, 0.3, 0.05, 0.3, color=(0.423, 0.423, 0.423))
    draw_box(4.53, 2.91, 7.533, 0.3, 0.05, 0.1, color=(0.423, 0.423, 0.423))
    
#==================================
#---------------End----------------
#==================================
    
#==================================
#-------------Bàn học--------------
#==================================
#Bàn học
def draw_table(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)

    #Kích thước mặt bàn 1
    table_width = 5.0
    table_depth = 3.0
    table_thickness = 0.2 #Độ dày mặt bàn
    table_height = 2.7 #Chiều cao từ mặt sàn tới bàn
    #Mặt bàn 2
    table_width_front = 5.1
    table_depth_front = 3.1
    table_thickness_front = 0.1
    table_height_front = 2.7
    #Mặt bàn 3
    table_width_front_3 = 4.9
    table_depth_front_3 = 3.0
    table_thickness_front_3 = 0.1
    table_height_front_3 = 1.8
    
    
    
    #Mặt bàn 1
    table_color = (1.0, 0.978, 0.9) #Chỉnh màu bàn
    draw_box(x_offset, table_height, z_offset, table_width, table_thickness, table_depth, table_color)
    
    #Mặt bàn 2
    table_color = (1.0, 0.9, 0.5)
    draw_box(x_offset, table_height_front, z_offset, table_width_front, table_thickness_front, table_depth_front, table_color)
    
   
    
    #Mặt bàn 3
    table_color = (1.0, 0.8588, 0.4627)
    draw_box(x_offset, table_height_front_3, z_offset, table_width_front_3, table_thickness_front_3, table_depth_front_3, table_color)
    
    #Kích thước chân bàn
    leg_w, leg_d, leg_h = 0.1, 0.1, table_height
    dx = table_width / 2 - leg_w / 2 #Khoảng cách từ tâm bàn đến rìa ngoài của bàn theo chiều ngang
    dz = table_depth / 2- leg_d / 2 #Khoảng cách từ tâm bàn đến rìa ngoài của bàn theo chiều sâu
    
    #Vị trí 4 chân bàn sát với mép bàn
    leg_color = (1.0, 0.978, 0.9)
    floor_y = -0.1
    draw_box(x_offset - dx, floor_y + leg_h / 10, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, floor_y + leg_h / 10, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset - dx, floor_y + leg_h / 10, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, floor_y + leg_h / 10, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)
    
    #Ngăn dưới 1
    box_w, box_d, box_h = 4.8, 0.1, 0.7
    box_y = 1.4 + box_h / 2 #Cách mặt bàn 0.5
    box_z = z_offset + (table_depth / 2) - (box_d / 2)
    
    #Vị trí ngăn bàn
    box_color = (1.0, 0.8588, 0.4627)
    draw_box(x_offset, box_y, box_z, box_w, box_h, box_d, color=box_color)
#==================================
#---------------End----------------
#==================================    
    

#==================================
#-----------Ghế học sinh-----------
#==================================

#Ghế học sinh
def draw_chair(x_offset= 0.5 , z_offset= -1.3, rotate=True, rotation_angle=0.0):
    glPushMatrix()
    floor_y = -0.1 #Ghế chạm mặt sàn
    # Kích thước mặt ghế
    seat_width = 1.7
    seat_depth = 1.7
    seat_thickness = 0.1
    seat_height = 1.5  # Chiều cao từ sàn đến mặt ghế
    
    if rotate:
        glRotatef(rotation_angle, 0, 1, 0)  # Xoay quanh trục Y
    
    # Mặt ghế
    seat_y = floor_y + seat_height + seat_thickness / 2 - 0.1
    seat_color = (1.0, 0.978, 0.9)
    draw_box(x_offset, seat_y, z_offset, seat_width, seat_thickness, seat_depth, color=seat_color)
    
    
    # Mặt ghế 2
    seat_width_2 = 1.7
    seat_depth_2 = 1.7
    seat_thickness_2 = 0.2
    seat_height_2 = 1.5  # Chiều cao từ sàn đến mặt ghế 2
    
    seat_y_2 = floor_y + seat_height_2 + seat_thickness_2 / 2 - 0.1
    seat_color_2 = (0.333, 0.431, 1.0)
    draw_box(x_offset, seat_y_2, z_offset, seat_width_2, seat_thickness_2, seat_depth_2, color=seat_color_2)
    


    # Kích thước chân ghế
    leg_w, leg_d, leg_h = 0.1, 0.1, seat_height
    dx = seat_width / 2 - leg_w / 2
    dz = seat_depth / 2 - leg_d / 2
    leg_color = (1.0, 0.978, 0.9)

    # 4 chân ghế
    leg_y = floor_y + leg_h / 10
    draw_box(x_offset - dx, leg_y, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, leg_y, z_offset - dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset - dx, leg_y, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)
    draw_box(x_offset + dx, leg_y, z_offset + dz, leg_w, leg_h, leg_d, color=leg_color)

    # Tựa lưng
    backrest_height = 1.0 #Độ dài
    backrest_thickness = 0.1 #Độ dày
    backrest_y = seat_y + backrest_height / 2 + 0.5 #Độ cao so với mặt sàn
    backrest_z = z_offset - seat_depth / 2 + backrest_thickness / 2
    backrest_color = (1.0, 0.978, 0.9) #Màu tựa lưng
    draw_box(x_offset, backrest_y, backrest_z, seat_width, backrest_height, backrest_thickness, color=(0.333, 0.431, 1.0))
    draw_box(x_offset, backrest_y + 0.2, backrest_z - 0.1, seat_width, backrest_height - 0.5, backrest_thickness, color=backrest_color)
    draw_box(x_offset - 0.5, backrest_y - 0.9, backrest_z - 0.1, seat_width - 1.6, backrest_height + 0.2, backrest_thickness, color=(1.0, 0.978, 0.9))
    draw_box(x_offset + 0.5, backrest_y - 0.9, backrest_z - 0.1, seat_width - 1.6, backrest_height + 0.2, backrest_thickness, color=(1.0, 0.978, 0.9))
    
    glPopMatrix()
#==================================
#---------------End----------------
#==================================

#==================================
#-------------Quyển Vở-------------
#==================================
   
def draw_note(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    #Quyển vở
    note_width_front_3 = 1.0
    note_depth_front_3 = 1.5
    note_thickness_front_3 = 0.1
    note_height_front_3 = 2.9

     #Quyển vở
     
    draw_box(x_offset, note_height_front_3, z_offset, note_width_front_3, note_thickness_front_3, note_depth_front_3, color=(1.0, 0.3, 0.2))

def draw_note2(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    #Quyển vở
    note_width_front_3 = 0.8
    note_depth_front_3 = 1.3
    note_thickness_front_3 = 0.1
    note_height_front_3 = 3.0

     #Quyển vở
    draw_box(x_offset, note_height_front_3, z_offset, note_width_front_3, note_thickness_front_3, note_depth_front_3, color = (0.1, 0.7, 0.2))

def draw_note3(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    #Quyển vở
    note_width_front_3 = 0.8
    note_depth_front_3 = 1.3
    note_thickness_front_3 = 0.1
    note_height_front_3 = 3.0

     #Quyển vở
    draw_box(x_offset, note_height_front_3 + 0.11, z_offset, note_width_front_3, note_thickness_front_3 - 0.09, note_depth_front_3, color = (0.1, 0.1, 0.7))
    draw_box(x_offset, note_height_front_3+ 0.01, z_offset, note_width_front_3 - 0.01, note_thickness_front_3, note_depth_front_3- 0.01, color = (0.9, 0.9, 0.9))
    draw_box(x_offset, note_height_front_3, z_offset, note_width_front_3, note_thickness_front_3 - 0.09, note_depth_front_3, color = (0.1, 0.1, 0.7))

def draw_note4(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    #Quyển vở
    note_width_front_3 = 0.8
    note_depth_front_3 = 1.3
    note_thickness_front_3 = 0.1
    note_height_front_3 = 3.0

     #Quyển vở
    draw_box(x_offset, note_height_front_3, z_offset, note_width_front_3, note_thickness_front_3, note_depth_front_3, color = (0.7, 0.2, 0.1))

#==================================
#---------------End----------------
#==================================

#==================================
#-------------Sách mở--------------
#==================================

def draw_book_open(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    draw_box(x_offset, 3.0, z_offset, 1.2, 0.1, 0.8, color = (0.1, 0.1, 0.6))
    draw_box(x_offset, 3.1, z_offset, 1.2, 0.01, 0.8, color = (0.9, 0.9, 0.9))
    draw_box(x_offset, 3.11, z_offset, 0.02, 0.01, 0.8, color = (0.3, 0.3, 0.3))


def draw_book_open2(x_offset = 0, z_offset = 0):
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    draw_box(x_offset, 3.0, z_offset, 1.4, 0.1, 0.9, color = (0.1, 0.6, 0.1))
    draw_box(x_offset, 3.1, z_offset, 1.37, 0.01, 0.9, color = (0.9, 0.9, 0.9))
    draw_box(x_offset, 3.11, z_offset, 0.02, 0.01, 0.8, color = (0.3, 0.3, 0.3))
    
#==================================
#---------------End----------------
#==================================

#==================================
#-------------Bảng đen-------------
#==================================
def draw_blackboard():
    # Kích thước bảng
    board_width = 9.0
    board_height = 6.0
    board_thickness = 0.2

    # Vị trí bảng gắn trên tường
    board_y = 3.0  # cao so với mặt sàn
    board_z = 11.7  # vị trí so với tường
    
    # Màu bảng
    board_color = (0.05, 0.09, 0.1)
    draw_box(0, board_y, board_z, board_width, board_height, board_thickness, color=board_color)
    
    #Khung bảng
    draw_box(0, board_y, board_z, 9.0, 0.2, board_thickness + 0.1, color=(1.0, 1.0, 1.0))
    draw_box(0, board_y + 6.0, board_z, 9.0, 0.2, board_thickness + 0.1, color=(1.0, 1.0, 1.0))
    draw_box(4.5, board_y, board_z, 0.2, 6.0, board_thickness + 0.1, color=(1.0, 1.0, 1.0))
    draw_box(-4.5, board_y, board_z, 0.2, 6.0, board_thickness + 0.1, color=(1.0, 1.0, 1.0))
    draw_box(0, board_y - 0.2, board_z - 0.5, 9.0, 0.2, board_thickness + 0.8, color=(0.918, 0.565, 0.0))

    #Kệ để sách
    draw_box(7.0, 6.0, board_z - 0.5, 2.0, 0.2, board_thickness + 0.5, color=(0.918, 0.565, 0.0))
    draw_box(7.0, 7.8, board_z - 0.5, 2.0, 0.2, board_thickness + 0.5, color=(0.918, 0.565, 0.0))
    #Sách trên kệ
    draw_box(6.2, 6.1, board_z - 0.5, 0.2, 1.2, board_thickness + 0.35, color=(0.039, 0.757, 0.0))
    draw_box(6.4, 6.1, board_z - 0.5, 0.2, 1.3, board_thickness + 0.35, color=(0.918, 0.2, 0.0))
    draw_box(6.8, 6.1, board_z - 0.5, 0.2, 1.2, board_thickness + 0.35, color=(0.2, 0.534, 0.918))
    draw_box(7.0, 6.1, board_z - 0.5, 0.2, 1.1, board_thickness + 0.35, color=(0.486, 0.486, 0.486))
    
#==================================
#---------------End----------------
#==================================

#==================================
#--------------Phấn----------------
#==================================

#Phấn
def draw_chalk(x= 4.0, y= 3.0, z= 11.0, length=1.0, radius=0.07):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(0, 1, 0, 0)  # Xoay để hình trụ nằm ngang (theo trục Z)
    glColor3f(1.0, 1.0, 1.0)  # Màu trắng

    quad = gluNewQuadric()
    gluCylinder(quad, radius, radius, length, 16, 1)

    # Đầu tròn phía sau
    glPushMatrix()
    glRotatef(180, 1, 0, 0)
    gluDisk(quad, 0, radius, 16, 1)
    glPopMatrix()

    # Đầu tròn phía trước
    glPushMatrix()
    glTranslatef(0, 0, length)
    gluDisk(quad, 0, radius, 16, 1)
    glPopMatrix()

    glPopMatrix()
#==================================
#---------------End----------------
#==================================

#==================================
#---------------Tủ-----------------
#==================================
    
def draw_cabinet():
    #vẽ tủ
    draw_box(5.0, 0, -11.5, 0.1, 8.0, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 1.0, -11.5, 0.1, 7.0, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(9.0, 0, -11.5, 0.1, 8.0, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 0, -11.5, 4.0, 0.2, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 1.0, -11.5, 4.0, 0.1, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 4.5, -11.5, 4.0, 0.1, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 7.9, -11.5, 4.1, 0.1, 1.5, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 0.0, -12.2, 4.1, 8.0, 0.1, color=(0.45, 0.45, 0.434))
    draw_box(7.0, 0.3, -10.7, 3.9, 0.8, 0.05, color=(0.765, 0.765, 0.765))
    draw_box(7.0, 0.7, -10.6, 0.7, 0.05, 0.05, color=(0.45, 0.45, 0.434))
    draw_box(6.0, 1.3, -10.7, 1.9, 3.2, 0.05, color=(0.765, 0.765, 0.765))
    draw_box(6.7, 2.5, -10.6, 0.05, 0.8, 0.05, color=(0.45, 0.45, 0.434))
    draw_box(6.0, 4.7, -10.7, 1.9, 3.2, 0.05, color=(0.765, 0.765, 0.765))
    draw_box(6.7, 5.9, -10.6, 0.05, 0.8, 0.05, color=(0.45, 0.45, 0.434))
    draw_box(8.0, 1.3, -10.7, 1.9, 3.2, 0.05, color=(0.765, 0.765, 0.765))
    draw_box(7.3, 2.5, -10.6, 0.05, 0.8, 0.05, color=(0.45, 0.45, 0.434))
    draw_box(8.0, 4.7, -10.7, 1.9, 3.2, 0.05, color=(0.765, 0.765, 0.765))
    draw_box(7.3, 5.9, -10.6, 0.05, 0.8, 0.05, color=(0.45, 0.45, 0.434))   

#==================================
#---------------End----------------
#==================================

#==================================
#------------Bảng chiếu------------
#==================================

def draw_cylinder1(radius=0.2, height=8.5, slices=32, stacks=1):
    glPushMatrix()
    glTranslatef(4.25, 9.5, 11.2)
    glColor3f(0.9, 1.0, 0.9)
    glRotatef(-90, 0, 1, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric, radius, radius, height, slices, stacks)
    gluDisk(quadric, 0, radius, slices, 1)  # Đáy
    glTranslatef(0, 0, height)
    gluDisk(quadric, 0, radius, slices, 1)  # Nắp
    glPopMatrix()


def draw_cylinder(radius=0.1, height=9.0, slices=32, stacks=1):
    glPushMatrix()
    glTranslatef(4.5, 9.5, 11.2)
    glColor3f(0.234, 0.234, 0.234)
    glRotatef(-90, 0, 1, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric, radius, radius, height, slices, stacks)
    gluDisk(quadric, 0, radius, slices, 1)  # Đáy
    glTranslatef(0, 0, height)
    gluDisk(quadric, 0, radius, slices, 1)  # Nắp
    glPopMatrix()
    draw_cylinder1()

def draw_frame():
    draw_box(4.5, 9.4, 11.6, 0.1, 0.3, 1.2, color=(0.45, 0.45, 0.434))
    draw_box(-4.5, 9.4, 11.6, 0.1, 0.3, 1.2, color=(0.45, 0.45, 0.434))

def draw_paper():
    draw_box(0.0, 3.7, 11.4, 8.5, 5.7, 0.01, color=(0.9, 1.0, 0.9))

#==================================
#---------------End----------------
#==================================

#==================================
#-------------Set Phím-------------
#==================================

def keyboard(key, x, y):
    global show_paper, light_on
    key = key.decode("utf-8")
    if key == 'p':
        show_paper = not show_paper
        glutPostRedisplay()
    elif key == 'l':
        light_on = not light_on
        if light_on:
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 0.925, 1.0])
        else:
            glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.3, 0.3, 0.3, 1.0])  # Ánh sáng tối hơn
        glutPostRedisplay()
    elif key == '\x1b':
        sys.exit()

#==================================
#---------------End----------------
#==================================

#==================================
#---------------Đèn----------------
#==================================

def draw_light():
    # Khung đèn
    draw_box(9.2, 9.0, 5.0, 0.1, 0.31, 5.1, color=(0.645, 0.645, 0.645))
    draw_box(9.2, 9.0, -5.0, 0.1, 0.31, 5.1, color=(0.645, 0.645, 0.645))
    
    # Bóng đèn (phát sáng khi light_on = True)
    if light_on:
        glMaterialfv(GL_FRONT, GL_EMISSION, [1.0, 1.0, 0.9, 1.0])  # Màu ánh sáng vàng nhạt
    else:
        glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])
    
    draw_box(9.2, 9.0, 5.0, 0.3, 0.3, 5.0, color=(1.0, 1.0, 0.9))
    draw_box(9.2, 9.0, -5.0, 0.2, 0.3, 5.0, color=(1.0, 1.0, 0.9))
    
    # Reset emission sau khi vẽ
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])



def draw_emissive_box(x, y, z, dx, dy, dz, color=(1.0, 1.0, 1.0), emissive=False):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(dx, dy, dz)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, color + (1.0,))
    
    if emissive:
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, color + (1.0,))
    else:
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, (0.0, 0.0, 0.0, 1.0))

    glutSolidCube(1.0)
    glPopMatrix()

#==================================
#---------------End----------------
#==================================

#==================================
#------------Thùng rác-------------
#==================================

def draw_trash_bin(radius=0.7, height=2.0, slices=32, stacks=1, thickness=0.05):
    glPushMatrix()
    glTranslatef(0.0, 0.17, 0.0)  # Vị trí gốc
    glColor3f(0.987, 0.987, 0.9)  # Màu xám thân ngoài

    # Thân ngoài
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric, radius, radius, height, slices, stacks)
    gluDisk(quadric, 0, radius, slices, 1)  # Đáy ngoài
    glPopMatrix()
    
    # Lòng trong rỗng
    glPushMatrix()
    glTranslatef(0.0, thickness, 0.0)
    glColor3f(0.9, 0.9, 0.9)  # Màu bên trong
    glRotatef(-90, 1, 0, 0)
    inner_radius = radius - thickness
    inner_height = height - thickness
    gluCylinder(quadric, inner_radius, inner_radius, inner_height, slices, stacks)
    glPopMatrix()

    glPopMatrix()
#==================================
#---------------End----------------
#==================================

#==================================
#------------Chậu cây--------------
#==================================
def draw_flower_pot():
    quadric = gluNewQuadric()

    # === CHẬU CÂY ===
    glPushMatrix()
    glColor3f(0.978, 0.978, 0.978)  # Màu nâu đất
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(-90, 1, 0, 0) # Xoay hệ tọa độ hiện tại quanh một trục cụ thể.
    # Hình côn cụt: đáy nhỏ, miệng lớn
    gluCylinder(quadric, 0.2, 0.2, 0.4, 32, 1)
    gluDisk(quadric, 0, 0.2, 32, 1)  # Đáy chậu
    glPopMatrix()

    # === ĐẤT ===
    glPushMatrix()
    glColor3f(0.36, 0.25, 0.2)  # Màu đất
    glTranslatef(0.0, 0.4, 0.0)  # Đặt đất bên trong chậu
    glRotatef(-90, 1, 0, 0)  # Xoay hệ tọa độ hiện tại quanh một trục cụ thể.
    gluDisk(quadric, 0, 0.2, 32, 1)
    glPopMatrix()

    # === THÂN CÂY ===
    glPushMatrix()
    glColor3f(0.396, 0.263, 0.129)  # Màu thân gỗ
    glTranslatef(0.0, 0.4, 0.0)  # bắt đầu từ mặt đất
    glRotatef(-90, 1, 0, 0) # Xoay hệ tọa độ hiện tại quanh một trục cụ thể.
    gluCylinder(quadric, 0.05, 0.05, 0.6, 16, 1)
    glPopMatrix()

    # === TÁN LÁ (các hình cầu) ===
    glPushMatrix()
    glColor3f(0.0, 0.8, 0.0)  # Xanh lá cây
    glTranslatef(0.0, 1.0, 0.0)
    glutSolidSphere(0.2, 16, 16)

    glTranslatef(0.15, 0.1, 0.0)
    glutSolidSphere(0.15, 16, 16)

    glTranslatef(-0.3, 0.0, 0.0)
    glutSolidSphere(0.15, 16, 16)

    glTranslatef(0.15, 0.1, 0.15)
    glutSolidSphere(0.15, 16, 16)

    glTranslatef(0.0, 0.0, -0.3)
    glutSolidSphere(0.15, 16, 16)
    glPopMatrix()
    
#==================================
#---------------End----------------
#==================================

#==================================
#---------Giấy kiểm tra------------
#==================================

def draw_paper_test(x_offset = 0.0, z_offset = 0.0):
    draw_box(x_offset, 2.0, z_offset, 1.2, 0.01, 1.6, color=(1.0, 1.0, 1.0))
    draw_box(x_offset, 2.01, z_offset, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.1, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.2, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.3, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.4, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.5, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  + 0.6, 0.9, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  - 0.6, 0.7, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  - 0.5, 0.5, 0.01, 0.01, color=(0.3, 0.3, 0.3))
    draw_box(x_offset, 2.01, z_offset  - 0.4, 0.5, 0.01, 0.01, color=(0.3, 0.3, 0.3))

#==================================
#---------------End----------------
#==================================

#==================================
#------------Gọi hàm---------------
#==================================
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Tính toán vị trí camera
    camX = radius * math.sin(math.radians(angle_h)) * math.cos(math.radians(angle_v))
    camY = radius * math.sin(math.radians(angle_v))
    camZ = radius * math.cos(math.radians(angle_h)) * math.cos(math.radians(angle_v))

    gluLookAt(camX, camY, camZ, 0, 0, 0, 0, 1, 0) # vecto(0, 1, 0) nghĩa là trục Y dương là hướng lên, giữ camera thẳng đứng, không bị lật nghiêng, Vector này giúp định hướng chính xác khung nhìn của camera.
    
    # Vẽ cảnh vật
    draw_floor()
    draw_wall()
    draw_chalk()
    draw_blackboard()
    draw_table_teacher(x_offset = 4.0, z_offset = 7.0)
    draw_PC()
    draw_folder()
    draw_frame()
    if show_paper:
        draw_paper()
    draw_cylinder()
    draw_light()

    # Vẽ tranh treo tường thứ nhất
    glPushMatrix()
    glTranslatef(0.0,0.5, 0.0)  # Vị trí tranh thứ nhất: x=9.2 (gần tường bên trái), y=5.6 (trên cao), z=0 (giữa phòng)
    draw_paint()
    glPopMatrix()


    #  # Vẽ tranh treo tường thứ hai
    # glPushMatrix()
    # glTranslatef(0.0,-2.5, 0.0)  # Vị trí tranh thứ nhất: x=9.2 (gần tường bên trái), y=5.6 (trên cao), z=0 (giữa phòng)
    # draw_paint()
    # glPopMatrix()

    # Vẽ tủ thứ nhất
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)  # Vị trí tủ thứ nhất: x=5.0 (sang phải), y=0.0 (sát sàn), z=-11.5 (gần tường sau)
    draw_cabinet()
    glPopMatrix()

    # # Vẽ tủ thứ hai
    # glPushMatrix()
    # glTranslatef(0.0, 0.0, 3.0)  # Vị trí tủ thứ hai: x=5.0 (cùng trục X), y=0.0 (sát sàn), z=-10.5 (trước tủ thứ nhất)
    # draw_cabinet()
    # glPopMatrix()

    # Vẽ thùng rác thứ nhất
    glPushMatrix()
    glTranslatef(4.0, 0.0, -11.5)
    draw_trash_bin()
    glPopMatrix()
    
    # # Vẽ thùng rác thứ hai
    # Trục X: Trái/phải, trục Y: lên/xuống(trên/dưới), trục Z: gần/xa
    # glPushMatrix()
    # glTranslatef(2.5, 0.0, -11.5) 
    # draw_trash_bin()
    # glPopMatrix()

    glPushMatrix()
    glTranslatef(5.0, 0.0, 0.0)  # Dịch sang phải để thùng rác thứ 2
    draw_trash_bin()
    glPopMatrix()
    
    #== Chậu cây ==
    glPushMatrix()
    glTranslatef(7.6, 6.2, 11.2)
    draw_flower_pot()
    glPopMatrix()
    #== Chậu cây ==/

    # glPushMatrix()
    # glTranslatef(7.2, 6.2, 11.2)  # Đặt bên trái chậu cây thứ nhất
    # draw_flower_pot()
    # glPopMatrix()
    
    #== Giấy kiểm tra ==
    glPushMatrix()
    glTranslatef(3.0, 3.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(45, 0, 1, 0)        # Quay 45 độ quanh trục Y
    glTranslatef(0.0, -2.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_paper_test(0.0, 0.0)
    glPopMatrix()
    #== Giấy kiểm tra==/
    
    #== Giấy kiểm tra2 ==
    glPushMatrix()
    glTranslatef(-3.0, 3.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-45, 0, 1, 0)        # Quay 45 độ quanh trục Y
    glTranslatef(0.0, -2.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_paper_test(0.0, 0.0)
    glPopMatrix()
    #== Giấy kiểm tra2==/
    
    #== Giấy kiểm tra3 ==
    glPushMatrix()
    glTranslatef(-4.0, 3.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-35, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, -2.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_paper_test(0.0, 0.0)
    glPopMatrix()
    #== Giấy kiểm tra3==/
    
    #== Giấy kiểm tra4 ==
    glPushMatrix()
    glTranslatef(-4.5, 3.01, 0.5)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(15, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, -2.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_paper_test(0.0, 0.0)
    glPopMatrix()
    #== Giấy kiểm tra4==/
    
    draw_chair(x_offset = 5.0, z_offset = -2.5, rotate=True, rotation_angle=-10)
    draw_chair(x_offset = 3.0, z_offset = -1.5)
    draw_chair(x_offset = -5.0, z_offset = -1.7)
    draw_chair(x_offset = -2.5, z_offset = -2.0, rotate=True, rotation_angle=10)
    draw_chair(x_offset = 5.0, z_offset = -7.3)
    draw_chair(x_offset = 4.0, z_offset = -6.5, rotate=True, rotation_angle=10)
    draw_chair(x_offset = -5.0, z_offset = -7.5)
    draw_chair(x_offset = -3.0, z_offset = -7.2)
    draw_table(x_offset = 4.0, z_offset = 0)
    draw_table(x_offset = -4.0, z_offset = 0)
    draw_table(x_offset = 4.0, z_offset = -6.0)
    draw_table(x_offset = -4.0, z_offset = -6.0)
    
    #== Vở 1 ==
    glPushMatrix()
    glTranslatef(5.0, 0.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(35, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_note(0.0, 0.0)
    glPopMatrix()
    #== Vở 1==/
    
    #== Vở 2 ==
    glPushMatrix()
    glTranslatef(5.0, 0.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(28, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_note2(0.0, 0.0)
    glPopMatrix()
    #== Vở 2==/
    
    #== Vở 3 ==
    glPushMatrix()
    glTranslatef(-5.0, 0.0, 0.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-30, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_note3(0.0, 0.0)
    glPopMatrix()
    #== Vở 3==/
    
    #== Vở 4 ==
    glPushMatrix()
    glTranslatef(-5.0, 0.0, -6.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-10, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_note4(0.0, 0.0)
    glPopMatrix()
    #== Vở 4==/
    
    #== Vở 5 ==
    glPushMatrix()
    glTranslatef(5.0, 0.0, -6.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-10, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_book_open(0.0, 0.0)
    glPopMatrix()
    #== Vở 5==/
    
    #== Vở 6 ==
    glPushMatrix()
    glTranslatef(-3.0, 0.0, -6.0)   # Dịch đến tâm tờ giấy (cùng chiều cao với draw_paper_test)
    glRotatef(-14, 0, 1, 0)        # Quay 28 độ quanh trục Y
    glTranslatef(0.0, 0.0, 0.0)  # Dịch ngược lại để giữ nguyên độ cao
    draw_book_open2(0.0, 0.0)
    glPopMatrix()
    #== Vở 6==/
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w/h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Classroom with Lighting")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
    

if __name__ == '__main__':
    main()

