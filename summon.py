import numpy as np
import cv2
import time
from PIL import Image, ImageDraw, ImageFont

import ollama
import os

from model_name_set import Model_Name




def wrap_text(text, max_width=70):
    """
    自动换行：一行不超过 max_width 字符
    """
    lines = []
    current_line = ""
    
    for char in text:
        # 尝试加下一个字符
        if len(current_line + char) > max_width:
            # 超过宽度 → 先保存当前行
            lines.append(current_line)
            current_line = char  # 新行从当前字符开始
        else:
            current_line += char
    
    # 最后一行
    if current_line:
        lines.append(current_line)
    
    return "\n".join(lines)
    


def role_speak(photo = "feibi.jpg", role_class="Ruler", text = "我是Ruler，准备召唤planer完成任务", photo_pos = [100, 80], dialog_box_pos = [350,80],  dialog_box_size = [600,180],font_size = 16 ):
    #photo = "feibi.jpg"
    photo_size = [220,180]
    
    photo_win_name = role_class
    
    dialog_box_color = [255,255,255]
    

    text_color = (255, 0, 0)  # RGB格式（红色）
    dialog_box_win_name = role_class + " say:"



    image = cv2.imread(photo)
    cv2.namedWindow(photo_win_name, cv2.WINDOW_NORMAL) 
    cv2.resizeWindow(photo_win_name, photo_size[0], photo_size[1])
    cv2.moveWindow(photo_win_name, photo_pos[0],photo_pos[1])
    cv2.imshow(photo_win_name, image)
    cv2.waitKey(1)


    # 对话框背景
    image_txt = 255*np.ones((dialog_box_size[1], dialog_box_size[0], 3), dtype=np.uint8)
    image_txt[:,:,0] =dialog_box_color[0] 
    image_txt[:,:,1] =dialog_box_color[1] 
    image_txt[:,:,2] =dialog_box_color[2] 

    # 使用pillow的复杂方法
    img_txt_pil = Image.fromarray(cv2.cvtColor(image_txt, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(img_txt_pil)

    font_path = "simhei.ttf"  # 替换为你的中文字体文件（如黑体、微软雅黑）

    font = ImageFont.truetype(font_path, font_size)

    position = (50, 50)  # (x, y)

    draw.text(position, text, font=font, fill=text_color)

    # 6. 将Pillow图像转回OpenCV格式
    img_txt_cv2 = cv2.cvtColor(np.array(img_txt_pil), cv2.COLOR_RGB2BGR)



    # 4. 显示图片
    cv2.namedWindow(dialog_box_win_name, cv2.WINDOW_NORMAL) 
    cv2.resizeWindow(dialog_box_win_name, dialog_box_size[0], dialog_box_size[1])
    cv2.moveWindow(dialog_box_win_name, dialog_box_pos[0], dialog_box_pos[1])

    cv2.imshow(dialog_box_win_name, img_txt_cv2)
    cv2.waitKey(1)  
    
'''
    print("sleep() is used for emulation the process of LLM.")
    for i in range(3):
        time.sleep(1)
        print("Time tick ", i)
    #cv2.destroyAllWindows()
'''

def main(model_name="gemma3:12b"):
    # clear the cmd
    os.system("cls") 
        
    messages = []
    
    while True:
        # prepare the input text
        ask_text = input("Master：")
        if ask_text in ["exit", "quit"]:
            break            
        messages.append({"role": "user", "content": ask_text})
        
        # close the cartoon for last chat
        cv2.destroyAllWindows()
        
        
        # display the ask cartoon
        role_speak(photo = "feibi.jpg", role_class="Master",text = ask_text,photo_pos = [50, 10], dialog_box_pos = [350,10],  dialog_box_size = [800,180])

        #call the ollama model to get the answer
        res = ollama.chat(model=model_name, messages=messages)       
        answer_text = res["message"]["content"]
        
        # wrap the answer text
        answer_text_wrap = wrap_text(answer_text)
        
        print("AI：", answer_text)
        messages.append({"role": "assistant", "content": answer_text})
        
        # display the answer cartoon
        role_speak(photo = "shenli.jpg", role_class="Servant", text = answer_text_wrap, photo_pos = [950, 230], dialog_box_pos = [50,230],dialog_box_size = [850,260])
        
        print("\nfinished one chat loop")
            
        
    
if __name__ == "__main__":
    main(model_name = Model_Name)
    
    