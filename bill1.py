import tkinter
from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
                           ### first Label Billing software
        bg_color="#074463"
        title=Label(root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
                                ##Variables
                             #####Cosmetic######
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

                          #####grocery variables######
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

                          #####Cold drink Variable######
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        
        ######Total product price and text variables
        self.cosmatic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink=StringVar()

        self.cosmatic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_tax=StringVar()
        ## customer details variable
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

             
    
                          ######Customer details Frame######
        f1=LabelFrame(root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        #### Custome name label and Entry box

        cname_lbl=Label(f1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white")
        cname_lbl.grid(column=0,row=0,padx=20,pady=5)
        cname_text=Entry(f1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN)
        cname_text.grid(row=0,column=1,pady=5,padx=10)
                      #### Custome phone number label and Entry box

        cphn_lbl=Label(f1,text="Phone No",font=("times new roman",18,"bold"),bg=bg_color,fg="white")
        cphn_lbl.grid(column=2,row=0,padx=20,pady=5)
        cphn_text=Entry(f1,width=15,font="arial 15",textvariable=self.c_phon,bd=7,relief=SUNKEN)
        cphn_text.grid(row=0,column=3,pady=5,padx=10)
                    ####Bill Number label and Entry box

        bill_lbl=Label(f1,text="Bill Number",font=("times new roman",18,"bold"),bg=bg_color,fg="white")
        bill_lbl.grid(column=4,row=0,padx=20,pady=5)
        bill_text=Entry(f1,width=15,font="arial 15",bd=7,textvariable=self.search_bill,relief=SUNKEN)
        bill_text.grid(row=0,column=5,pady=5,padx=10)
          ####First Button
        btn1=Button(f1,text="Search",width=10,bd=7,command=self.find_bill,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

                        #### Cosmatic 2nd Frame

        f2=LabelFrame(root,text="Cosmatic",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)
                        ### Label (Bath Soap) and entery in Cosmatic frame
        bath_lbl=Label(f2,text="Bath Soap",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        bath_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text=Entry(f2,width=10,font="arial 15",textvariable=self.soap,bd=5,relief=SUNKEN)
        bath_text.grid(row=0,column=1,padx=10,pady=10)

                      ### Label (Face cream) and entery in Cosmatic frame
        face_c_lbl=Label(f2,text="Face Cream",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        face_c_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_c_text=Entry(f2,width=10,font="arial 15",textvariable=self.face_cream,bd=5,relief=SUNKEN)
        face_c_text.grid(row=1,column=1,padx=10,pady=10)

                     ### Label (Face wash) and entery in Cosmatic frame
        face_w_lbl=Label(f2,text="Face wash",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        face_w_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_text=Entry(f2,width=10,font="arial 15",bd=5,textvariable=self.face_wash,relief=SUNKEN)
        face_w_text.grid(row=2,column=1,padx=10,pady=10)

                     ### Label (hair spray) and entery in Cosmatic frame
        hair_lbl=Label(f2,text="Hair Spray",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        hair_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_text=Entry(f2,width=10,font="arial 15",bd=5,textvariable=self.spray,relief=SUNKEN)
        hair_text.grid(row=3,column=1,padx=10,pady=10)

                  ### Label (hair Gell) and entery in Cosmatic frame
        hair_g_lbl=Label(f2,text="Hair Gell",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        hair_g_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_text=Entry(f2,width=10,font="arial 15",bd=5,textvariable=self.gell,relief=SUNKEN)
        hair_g_text.grid(row=4,column=1,padx=10,pady=10)

                  ### Label (Body Loshan) and entery in Cosmatic frame
        body_lbl=Label(f2,text="Body Loshan",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        body_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_text=Entry(f2,width=10,font="arial 15",bd=5,textvariable=self.loshan,relief=SUNKEN)
        body_text.grid(row=5,column=1,padx=10,pady=10)


            #### Grocery 3rd Frame

        f3=LabelFrame(root,text="Grocery",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f3.place(x=340,y=180,width=325,height=380)
                        ### Label (rice) and entery in 3rd frame
        rice_lbl=Label(f3,text="Rice",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        rice_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.rice,relief=SUNKEN)
        rice_text.grid(row=0,column=1,padx=10,pady=10)

                      ### Label (Food oil) and entery in 3rd
        food_lbl=Label(f3,text="Food Oil",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        food_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.food_oil,relief=SUNKEN)
        food_text.grid(row=1,column=1,padx=10,pady=10)

                     ### Label (Daal) and entery in 3rd frame
        daal_lbl=Label(f3,text="Daal",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        daal_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.daal,relief=SUNKEN)
        daal_text.grid(row=2,column=1,padx=10,pady=10)

                     ### Label (Wheat) and entery in 3rd frame
        wht_lbl=Label(f3,text="Wheat",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        wht_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wht_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.wheat,relief=SUNKEN)
        wht_text.grid(row=3,column=1,padx=10,pady=10)

                  ### Label (Sugar) and entery in 3rd frame
        sug_lbl=Label(f3,text="Sugar",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        sug_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sug_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.sugar,relief=SUNKEN)
        sug_text.grid(row=4,column=1,padx=10,pady=10)

                  ### Label (Tea) and entery in 3rd frame
        t_lbl=Label(f3,text="Tea",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        t_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        t_text=Entry(f3,width=10,font="arial 15",bd=5,textvariable=self.tea,relief=SUNKEN)
        t_text.grid(row=5,column=1,padx=10,pady=10)



                       #### Cold drink 4th Frame

        f4=LabelFrame(root,text="Cold Drink",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f4.place(x=670,y=180,width=325,height=380)
                        ### Label (Maza) and entery in 4th frame
        maza_lbl=Label(f4,text="Maza",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        maza_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.maza,relief=SUNKEN)
        maza_text.grid(row=0,column=1,padx=10,pady=10)

                      ### Label (Cock) and entery in 4th
        cock_lbl=Label(f4,text="Cock",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        cock_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cock_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.cock,relief=SUNKEN)
        cock_text.grid(row=1,column=1,padx=10,pady=10)

                     ### Label (Frooti) and entery in 4th frame
        fr_lbl=Label(f4,text="Frooti",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        fr_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        fr_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.frooti,relief=SUNKEN)
        fr_text.grid(row=2,column=1,padx=10,pady=10)

                     ### Label (Thumbs Up) and entery in 4th frame
        up_lbl=Label(f4,text="Thumbs Up",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        up_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        up_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.thumbsup,relief=SUNKEN)
        up_text.grid(row=3,column=1,padx=10,pady=10)

                  ### Label (Limca) and entery in 4th frame
        lm_lbl=Label(f4,text="Limca",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        lm_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lm_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.limca,relief=SUNKEN)
        lm_text.grid(row=4,column=1,padx=10,pady=10)

                  ### Label (sprite) and entery in 3rd frame
        sp_lbl=Label(f4,text="Sprite",font=("times new roman",18,"bold"),bg=bg_color,fg="lightgreen")
        sp_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sp_text=Entry(f4,width=10,font="arial 15",bd=5,textvariable=self.sprite,relief=SUNKEN)
        sp_text.grid(row=5,column=1,padx=10,pady=10)

                            #############  Bill area 5th Frame
        f5=Frame(root,bd=10,relief=GROOVE)
        f5.place(x=1010,y=180,width=350,height=380)
                    ### label in 5th frame
        bill_title=Label(f5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        ####### Bill menu 6th frame
    
        f6=LabelFrame(root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=140)
            ### label (total cosmatic price) in bill menu frAME
        m1=Label(f6,text="Total Cosmetic Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cosmatic_price,relief=SUNKEN)
        m1_text.grid(row=0,column=1,padx=10,pady=1)
            ## label (total Grocery price) in bill menu frame
        m2=Label(f6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.grocery_price,relief=SUNKEN)
        m2_text.grid(row=1,column=1,padx=10,pady=1)

        ## label (total cold drink price) in bill menu frame
        m3=Label(f6,text="Total cold_drink price",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cold_drink,relief=SUNKEN)
        m3_text.grid(row=2,column=1,padx=10,pady=1)

        c1=Label(f6,text="Cosmetic tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cosmatic_tax,relief=SUNKEN)
        c1_text.grid(row=0,column=3,padx=10,pady=1)
            ## label ( Grocery tax) in bill menu frame
        c2=Label(f6,text="Grocery tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.grocery_tax,relief=SUNKEN)
        c2_text.grid(row=1,column=3,padx=10,pady=1)

        ## label ( cold drink tex) in bill menu frame
        c3=Label(f6,text="cold drink tax",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text=Entry(f6,width=18,font="arial 10 bold",bd=7,textvariable=self.cold_tax,relief=SUNKEN)
        c3_text.grid(row=2,column=3,padx=10,pady=1)
       #### Button frame in Bill menu frame
        btn_frame=Frame(f6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=580,height=105)

        ###   Buttons in Button frame
        total_bt=Button(btn_frame,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        g_bt=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_bt=Button(btn_frame,text="Clear",bg="cadetblue",command=self.clear,fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_bt=Button(btn_frame,text="Exit",bg="cadetblue",command=self.exit_app,fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
            ### functionallity###
    def total(self):
            #### cosmatic functionality
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*120
        self.c_sp_p=self.spray.get()*180
        self.c_g_p=self.gell.get()*140
        self.c_los_p=self.loshan.get()*180
        self.total_cosmatic_price=float(
                       self.c_s_p+
                       self.c_fc_p+
                       self.c_fw_p+
                       self.c_sp_p+
                       self.c_g_p+
                       self.c_los_p
        )
        self.cosmatic_price.set(str(self.total_cosmatic_price))
        self.cosmatic_tax.set(str(self.total_cosmatic_price*0))

                      ###grocery functionality
        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_da_p=self.daal.get()*60
        self.g_wh_p=self.wheat.get()*240
        self.g_sug_p=self.sugar.get()*65
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                       self.g_r_p+
                       self.g_fo_p+
                       self.g_da_p+
                       self.g_wh_p+
                       self.g_sug_p+
                       self.g_t_p
                       )           
        self.grocery_price.set(str(self.total_grocery_price))
        self.grocery_tax.set(str(self.total_grocery_price*0))

                    ###cold drink functionality
        self.d_m_p=self.maza.get()*30
        self.d_cock_p=self.cock.get()*30
        self.d_f_p=self.frooti.get()*50
        self.d_up_p=self.thumbsup.get()*45
        self.d_li_p=self.limca.get()*30
        self.d_sp_p=self.sprite.get()*30
        self.total_cold_drink_price=float(
                       self.d_m_p+
                       self.d_cock_p+
                       self.d_f_p+
                       self.d_up_p+
                       self.d_li_p+
                       self.d_sp_p
                       )           
        self.cold_drink.set(str(self.total_cold_drink_price))
        self.cold_tax.set(str(self.total_cold_drink_price*0))

        self.total_bill=float(self.total_cosmatic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price
                            )

    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"Welcome Webcode Reatil\n")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.txtarea.insert(END,f"\n =====================================")
        self.txtarea.insert(END,f"\nproducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n =====================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details must required")
        elif self.cosmatic_price.get()=="0.0" and self.grocery_price.get()=="0.0"and self.cold_drink.get()=="0.0":
            messagebox.showerror("Error","No product selected")
        else:
         self.welcome_bill()

             #### cosmatic condition
         if self.soap.get()!=0:
          self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
         if self.face_cream.get()!=0:
          self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
         if self.face_wash.get()!=0:
          self.txtarea.insert(END,f"\nFace wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
         if self.spray.get()!=0:
          self.txtarea.insert(END,f"\nHair Spray\t\t{self.spray.get()}\t\t{self.c_sp_p}")
         if self.gell.get()!=0:
          self.txtarea.insert(END,f"\nHair Gell\t\t{self.gell.get()}\t\t{self.c_g_p}")
         if self.loshan.get()!=0:
          self.txtarea.insert(END,f"\nBody Loshan\t\t{self.loshan.get()}\t\t{self.c_los_p}")

                   #### Grocey condition
         if self.rice.get()!=0:
          self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
         if self.food_oil.get()!=0:
          self.txtarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
         if self.daal.get()!=0:
          self.txtarea.insert(END,f"\nDaal\t\t{self.daal.get()}\t\t{self.g_da_p}")
         if self.wheat.get()!=0:
          self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_wh_p}")
         if self.sugar.get()!=0:
          self.txtarea.insert(END,f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_sug_p}")
         if self.tea.get()!=0:
          self.txtarea.insert(END,f"\nTea\t\t{self.tea.get()}\t\t{self.g_t_p}")

        #### Cold Drink condition
         if self.maza.get()!=0:
          self.txtarea.insert(END,f"\nMaza\t\t{self.maza.get()}\t\t{self.d_m_p}")
         if self.cock.get()!=0:
          self.txtarea.insert(END,f"\nCock\t\t{self.cock.get()}\t\t{self.d_cock_p}")
         if self.frooti.get()!=0:
          self.txtarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
         if self.thumbsup.get()!=0:
          self.txtarea.insert(END,f"\nThumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_up_p}")
         if self.limca.get()!=0:
          self.txtarea.insert(END,f"\nSugar\t\t{self.limca.get()}\t\t{self.d_li_p}")
         if self.sprite.get()!=0:
          self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t\t{self.d_sp_p}")

        self.txtarea.insert(END,f"\n===================================")
               ###pending this step
        #if self.cosmatic_tax.get()!=0.0:
            #self.txtarea.insert(END,f"\nCosmatic Tax\t\t\t{self.cosmatic_tax.get()}")
        #if self.grocery_tax.get()!=0.0:
            #self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        #if self.cold_tax.get()!=0.0:
            #self.txtarea.insert(END,f"\nCold Drink Tax\t\t\t{self.cold_tax.get()}")
        self.txtarea.insert(END,f"\nTotal Bill\t\t\t{self.total_bill}")


        self.txtarea.insert(END,f"\n===================================")
        self.save_bill()
      ##### Saved bill functionality
    def  save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save this bill")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no :{self.bill_no.get()} saved successfully")
        else:
            return 
              ###### Search button functionallity
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","invalid bill no")    

     #### Clear Button Functionallity
    def clear(self):
                                     #####Cosmetic######
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)

                          #####grocery variables######
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

                          #####Cold drink Variable######
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        
        ######Total product price and text variables
        self.cosmatic_price.set("")
        self.grocery_price.set("")
        self.cold_drink.set("")

        self.cosmatic_tax.set("")
        self.grocery_tax.set("")
        self.cold_tax.set("")
        ## customer details variable
        self.c_name.set("")
        self.c_phon.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()
     ### Exit Button functionallity
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit ")
        if op>0:
            self.root.destroy()



root=Tk()
obj =Bill_app(root)
root.mainloop()

