
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

"""
เลขโรมัน

"""


if __name__=='__main__':

    while True:
        print("\n")
        print("ถ้าต้องการออกจากลูป กรอก'exit'")
        data_input = input("กรอกเลขอารบิคที่ต้องการแปลงเป็นเลขโรมัน: ")
        spliting_data_input = list(data_input)

        # ตัวแปรที่ใช้ทดสอบค่าที่รับมาว่าใช่ตัวเลขอารบิคหรือไม่
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        spliting_letters = list(letters)
        
        th_letters = 'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝภภมรลวศษสหฬอฮ'
        spliting_th_letters = list(th_letters)

        numbers = '1234567890'
        spliting_numbers = list(numbers)

        if data_input == 'exit':
            break
        else: 
            checked = []  
            for item in spliting_data_input:
                if item in spliting_letters:
                    checked = False
                    break
                elif item in spliting_th_letters:
                    checked = False
                    break
                elif item in spliting_numbers:
                    checked = True
                    break
           
            if checked == False:
                print("Error, ตัวเลขอารบิคเท่านั้น!")
            else:
                int_data_input = int(data_input)
                if int_data_input >= 0 and int_data_input < 1001:
                    if int_data_input == 0:
                        print(f"Error, ไม่มี {int_data_input} ในเลขโรมัน!")
                    elif int_data_input > 0 and int_data_input < 1001:
                        """ตัวแปรเลขโรมัน"""
                        thouands = ['', 'M']
                        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
                        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
                        units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
                        th4 = thouands[int_data_input//1000] #หลักพัน
                        rd3 = hundreds[(int_data_input%1000)//100] #หลักร้อย
                        nd2 = tens[(int_data_input%100)//10] # หลักสิบ
                        st1 = units[(int_data_input%10)//1] # หลักหน่วย
                        result = th4 + rd3 + nd2 + st1
                        print(f'เลขโรมัน: {result}')
                          
                elif int_data_input > 1000:
                    print(f"Error,{int_data_input} ตัวเลขเกิน 1000!")
                else:
                    print(f"Error,{int_data_input} ตัวเลขติดลบ!") 
                

              

              

                    
                    
                    
                    
            



        
