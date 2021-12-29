from tkinter import messagebox
from tkinter.ttk import Combobox

import pymysql
from config import *
from tkinter import *

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected")

    try:
        # create table users
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(`id` int(11) NOT NULL AUTO_INCREMENT," \
        #                          "`login` varchar(30) NOT NULL," \
        #                          "`password` varchar(30) NOT NULL," \
        #                          "PRIMARY KEY (`id`));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (login, password) VALUES ('anastasia','123');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("User added successfully")
        # select all data from table

        # with connection.cursor() as cursor:
        #     insert_query = f"INSERT INTO `users` (login, password) VALUES ('{login}','{password}');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("User added successfully")

        # with connection.cursor() as cursor:
        #     select_all_query = "SELECT * FROM `users`;"
        #     cursor.execute(select_all_query)
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        list_of_tables = ['batches', 'countries', 'plants', 'manufactoring', 'orders', 'paints', 'paint_subtypes', 'paint_types', 'plants','resources','resource_types','storages', 'workers','worker_types']



        def create_list():
            list_window = Toplevel(root)
            root.withdraw()
            list_window.geometry('600x450')
            list_window.resizable(width=True, height=True)

            canvas = Canvas(list_window, height=300, width=250)
            canvas.pack()

            frame = Frame(list_window, bg='beige')
            frame.place(relwidth=1, relheight=1)

            title = Label(frame, text='Производство краски', font='Times 14')
            title.pack()

            def on_closing():
                list_window.destroy()
                root.deiconify()

            list_window.protocol("WM_DELETE_WINDOW", on_closing)

            def change_table(event):
                for widget in list_frame.winfo_children():
                    widget.destroy()
                with connection.cursor() as cursor:
                    table_name = str(list.get())
                    current_table = table_name
                    if len(table_name) < 1:
                        label = Label(list_frame, text="Пока здесь ничего нет")
                        label.pack()
                    else:
                        select_all_query = f"SELECT * FROM `{table_name}`"
                        cursor.execute(select_all_query)
                        rows = cursor.fetchall()
                        if len(rows) < 1:
                            label = Label(list_frame, text="Пока здесь ничего нет")
                            label.pack()
                        else:
                            for row in rows:
                                if current_table == 'batches':
                                    label = Label(list_frame, text="Number: "+str(row["batch_number"])+" Name: "+str(row["batch_name"])+" Plant number: "+str(row["plant_number"]))
                                    label.pack()
                                elif current_table == 'countries':
                                    label = Label(list_frame, text="Code: "+str(row["country_code"])+" Name: "+str(row["country_name"]))
                                    label.pack()
                                elif current_table == 'manufactoring':
                                    label = Label(list_frame, text="Date: "+str(row["date_of_manufactoring"])+" Produced paint: "+str(row["produced_paint"])+" Discarded paint: "+str(row["discarded_paint"])+" Time: "+str(row["time_for_manufactoring"]))
                                    label.pack()
                                elif current_table == 'orders':
                                    label = Label(list_frame, text="Number: "+str(row["order_number"])+" Description: "+str(row["order_description"]))
                                    label.pack()
                                elif current_table == 'paints':
                                    label = Label(list_frame, text="Number: "+str(row["paint_number"])+" Name: "+str(row["paint_name"])+" Color: "+str(row["color"])+" Subtype code: "+str(row["paint_subtype_code"])+" Batch number: "+str(row["batch_number"])+" Date: "+str(row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'paint_subtypes':
                                    label = Label(list_frame, text="Code: "+str(row["type_code"])+" Name: "+str(row["type_name"])+" Description: "+str(row["type_description"])+" Type code: "+str(row["paint_type_code"]))
                                    label.pack()
                                elif current_table == 'paint_types':
                                    label = Label(list_frame, text="Code: "+str(row["type_code"])+" Name: "+str(row["type_name"])+" Description: "+str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'plants':
                                    label = Label(list_frame, text="Number: "+str(row["plant_number"])+" Name: "+str(row["plant_name"])+" Address: "+str(row["address"])+" Country code: "+str(row["country_code"])+" Order num: "+str(row["order_number"]))
                                    label.pack()
                                elif current_table == 'resources':
                                    label = Label(list_frame, text="Code: "+str(row["resource_code"])+" Name: "+str(row["resource_name"])+" Storage num: "+str(row["storage_number"])+" Type code: "+str(row["type_code"])+" Date: "+str(row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'resource_types':
                                    label = Label(list_frame, text="Code: "+str(row["type_code"])+" Name: "+str(row["type_name"])+" Description: "+str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'storages':
                                    label = Label(list_frame, text="Number: "+str(row["storage_number"])+" Name: "+str(row["storage_name"])+" Address: "+str(row["address"]))
                                    label.pack()
                                elif current_table == 'workers':
                                    label = Label(list_frame, text="Code: "+str(row["worker_code"])+" Name: "+str(row["worker_name"])+" Plant num: "+str(row["plant_number"])+" Type code: "+str(row["worker_type_code"]))
                                    label.pack()
                                elif current_table == 'worker_types':
                                    label = Label(list_frame, text="Code: "+str(row["type_code"])+" Name: "+str(row["type_name"])+" Description: "+str(row["type_description"]))
                                    label.pack()
                                # id = str(row["id"])
                                # name = str(row["name"])
                                # artist = str(row["artist"])
                                # label = Label(list_frame, text=id + ". " + name + " - " + artist)

            list = Combobox(frame, width=50, height=20, values=list_of_tables, state="readonly")
            list.bind("<<ComboboxSelected>>", change_table)
            list.pack()

            list_frame = Frame(frame, bg='white')
            list_frame.pack()

            def refresh_page():
                list_window.destroy()
                create_list()

            def add_record():
                print(str(list.get()))
                add_window = Toplevel(list_window)
                list_window.withdraw()
                add_window.geometry('450x400')
                add_window.resizable(width=True, height=True)

                canvas = Canvas(add_window, height=300, width=250)
                canvas.pack()

                frame = Frame(add_window, bg='beige')
                frame.place(relwidth=1, relheight=1)

                title = Label(frame, text='Добавить запись')
                title.pack()

                def on_closing():
                    add_window.destroy()
                    list_window.deiconify()

                add_window.protocol("WM_DELETE_WINDOW", on_closing)

                if str(list.get()) == '':
                    messagebox.showerror(title='Ошибка', message='Выберите таблицу')
                # BATCHES
                elif str(list.get()) == 'batches':

                    label2 = Label(frame, text='Name:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Plant number:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    def add_in_list():
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(value2) < 1 or len(value3) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `batches` VALUES ('','{value2}','{value3}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()

                # COUNTRIES
                elif str(list.get()) == 'countries':

                    label2 = Label(frame, text='Name:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()


                    def add_in_list():
                        value2 = str(field2.get())

                        if len(value2) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `countries` VALUES ('','{value2}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()

                # PLANTS
                elif str(list.get()) == 'plants':

                    label2 = Label(frame, text='Name:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Address:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()
                    label4 = Label(frame, text='Country code:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()
                    label5 = Label(frame, text='Order num:')
                    label5.pack()
                    field5 = Entry(frame, bg='white')
                    field5.pack()

                    def add_in_list():
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())
                        value5 = str(field5.get())

                        if len(value2) < 1 or len(value3) < 1 or len(value4) < 1 or len(value5) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `plants` VALUES ('','{value2}','{value3}','{value4}','{value5}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()

                # MANUFACTORING
                elif str(list.get()) == 'manufactoring':

                    label3 = Label(frame, text='Produced paint:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()
                    label4 = Label(frame, text='Discarded paint:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()
                    label5 = Label(frame, text='Time:')
                    label5.pack()
                    field5 = Entry(frame, bg='white')
                    field5.pack()

                    def add_in_list():
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())
                        value5 = str(field5.get())

                        if len(value3) < 1 or len(value4) < 1 or len(value5) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `manufactoring` VALUES ('','{value3}','{value4}','{value5}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # ORDERS
                elif str(list.get()) == 'orders':

                    label1 = Label(frame, text='Description:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    def add_in_list():
                        value1 = str(field1.get())

                        if len(value1) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `orders` VALUES ('','{value1}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # PAINTS
                elif str(list.get()) == 'paints':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Subtype code:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Batch number:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Date:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    label5 = Label(frame, text='Color:')
                    label5.pack()
                    field5 = Entry(frame, bg='white')
                    field5.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())
                        value5 = str(field5.get())

                        if len(value1) < 1 or len(value2) < 1 or len(value3) < 1 or len(value4) < 1 or len(value5) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `paints` VALUES ('','{value1}','{value2}','{value3}','{value4}','{value5}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # PAINT_SUBTYPES
                elif str(list.get()) == 'paint_subtypes':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Description:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Paint type code:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(value1) < 1 or len(value2) < 1 or len(value3) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `paint_subtypes` VALUES ('','{value1}','{value2}','{value3}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # PAINT_TYPES
                elif str(list.get()) == 'paint_types':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Description:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(value1) < 1 or len(value2) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `paint_types` VALUES ('','{value1}','{value2}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # PLANTS
                elif str(list.get()) == 'plants':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Address:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Country code:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Order number:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())

                        if len(value1) < 1 or len(value2) < 1 or len(value3) < 1 or len(value4) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `plants` VALUES ('','{value1}','{value2}','{value3}','{value4}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # RESOURCES
                elif str(list.get()) == 'resources':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Storage number:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Type code:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Date:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())

                        if len(value1) < 1 or len(value2) < 1 or len(value3) < 1 or len(value4) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `resources` VALUES ('','{value1}','{value2}','{value3}','{value4}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # RESOURCE_TYPES
                elif str(list.get()) == 'resource_types':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Description:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(value1) < 1 or len(value2) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `resource_types` VALUES ('','{value1}','{value2}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # STORAGES
                elif str(list.get()) == 'storages':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Address:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(value1) < 1 or len(value2) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `storages` VALUES ('','{value1}','{value2}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # WORKERS
                elif str(list.get()) == 'workers':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Plant number:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Type code:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(value1) < 1 or len(value2) < 1 or len(value3) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `workers` VALUES ('','{value1}','{value2}','{value3}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()
                # WORKER_TYPES
                elif str(list.get()) == 'workers':

                    label1 = Label(frame, text='Name:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Description:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def add_in_list():
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(value1) < 1 or len(value2) < 1:
                            messagebox.showerror(title='Ошибка', message='Заполните все поля')
                        else:
                            with connection.cursor() as cursor:
                                insert_query = f"INSERT INTO `worker_types` VALUES ('','{value1}','{value2}');"
                                cursor.execute(insert_query)
                                connection.commit()
                                messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                add_window.destroy()
                                refresh_page()

                    btn_add = Button(frame, text='Добавить', command=add_in_list)
                    btn_add.pack()

                def return_back():
                    add_window.destroy()
                    list_window.deiconify()

                btn_back = Button(frame, text='Назад', command=return_back)
                btn_back.pack()

            def add_plant():
                add_window = Toplevel(list_window)
                list_window.withdraw()
                add_window.geometry('450x400')
                add_window.resizable(width=True, height=True)

                canvas = Canvas(add_window, height=300, width=250)
                canvas.pack()

                frame = Frame(add_window, bg='beige')
                frame.place(relwidth=1, relheight=1)

                title = Label(frame, text='Добавить запись')
                title.pack()
                label1 = Label(frame, text='Number:')
                label1.pack()
                field1 = Entry(frame, bg='white')
                field1.pack()

                label2 = Label(frame, text='Name:')
                label2.pack()
                field2 = Entry(frame, bg='white')
                field2.pack()

                label3 = Label(frame, text='Address:')
                label3.pack()
                field3 = Entry(frame, bg='white')
                field3.pack()

                label4 = Label(frame, text='Country code:')
                label4.pack()
                field4 = Entry(frame, bg='white')
                field4.pack()

                label5 = Label(frame, text='Order num:')
                label5.pack()
                field5 = Entry(frame, bg='white')
                field5.pack()

                def add_in_list():
                    value1 = str(field1.get())
                    value2 = str(field2.get())
                    value3 = str(field3.get())
                    value4 = str(field4.get())
                    value5 = str(field5.get())

                    if len(value1) < 1 or len(value2) < 1 or len(value3) < 1 or len(value4) < 1 or len(value5) < 1:
                        messagebox.showerror(title='Ошибка', message='Заполните все поля')
                    else:
                        with connection.cursor() as cursor:
                            insert_query = f"INSERT INTO `plants` VALUES ('{value1}','{value2}','{value3}','{value4}','{value5}');"
                            cursor.execute(insert_query)
                            connection.commit()
                            messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                            add_window.destroy()
                            refresh_page()

                btn_add = Button(frame, text='Добавить', command=add_in_list)
                btn_add.pack()

                def return_back():
                    add_window.destroy()
                    list_window.deiconify()

                btn_back = Button(frame, text='Назад', command=return_back)
                btn_back.pack()

















            def add_song():
                if current_table == '':
                    messagebox.showerror(title='Ошибка', message='Выберите таблицу')
                else:
                    add_window = Toplevel(list_window)
                    list_window.withdraw()
                    add_window.geometry('450x400')
                    add_window.resizable(width=True, height=True)

                    canvas = Canvas(add_window, height=300, width=250)
                    canvas.pack()

                    frame = Frame(add_window, bg='beige')
                    frame.place(relwidth=1, relheight=1)

                    title = Label(frame, text='Добавить запись')
                    title.pack()
                    if (current_table == 'batches'):
                        label1 = Label(frame, text='Number:')
                        label1.pack()
                        field1 = Entry(frame, bg='white')
                        field1.pack()

                        label2 = Label(frame, text='Name:')
                        label2.pack()
                        field2 = Entry(frame, bg='white')
                        field2.pack()

                        label3 = Label(frame, text='Plant number:')
                        label3.pack()
                        field3 = Entry(frame, bg='white')
                        field3.pack()

                        def add_in_list():
                            value1 = str(field1.get())
                            value2 = str(field2.get())
                            value3 = str(field3.get())

                            if len(value1) < 1 or len(value2) < 1 or len(value3) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните все поля')
                            else:
                                with connection.cursor() as cursor:
                                    insert_query = f"INSERT INTO `{current_table}` VALUES ('{value1}','{value2}','{value3}');"
                                    cursor.execute(insert_query)
                                    connection.commit()
                                    messagebox.showinfo(title='Название', message='Запись добавлена успешно')
                                    add_window.destroy()
                                    refresh_page()


                        btn_add = Button(frame, text='Добавить', command=add_in_list)
                        btn_add.pack()

                    def return_back():
                        add_window.destroy()
                        list_window.deiconify()

                    btn_back = Button(frame, text='Назад', command=return_back)
                    btn_back.pack()


            def update_song():
                update_window = Toplevel(list_window)
                list_window.withdraw()
                update_window.geometry('450x400')
                update_window.resizable(width=True, height=True)

                canvas = Canvas(update_window, height=300, width=250)
                canvas.pack()

                frame = Frame(update_window, bg='beige')
                frame.place(relwidth=1, relheight=1)

                title = Label(frame, text='Изменить запись')
                title.pack()

                def on_closing():
                    update_window.destroy()
                    list_window.deiconify()

                update_window.protocol("WM_DELETE_WINDOW", on_closing)

                # BATCHES
                if str(list.get()) == 'batches':
                    id_label = Label(frame, text='Введите номер/код записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый номер завода:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите номер/код')
                        else:
                            if len(value1) < 1 and len(value2) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `batches` SET `batch_name`='{value1}' WHERE `batch_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `batches` SET `plant_number`='{value2}' WHERE `batch_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()

                # COUNTRIES
                if str(list.get()) == 'countries':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `countries` SET `country_name`='{value1}' WHERE `country_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # MANUFACTORING
                if str(list.get()) == 'manufactoring':
                    id_label = Label(frame, text='Введите дату изготовления:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое количество произведенной краски:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новое количество списанной краски:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новое время изготовления:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()


                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите дату')
                        else:
                            if len(value1) < 1 and len(value2) < 1 and len(value3) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `manufactoring` SET `produced_paint`='{value1}' WHERE `date_of_manufactoring`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `manufactoring` SET `discarded_paint`='{value2}' WHERE `date_of_manufactoring`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `manufactoring` SET `time_for_manufactoring`='{value3}' WHERE `date_of_manufactoring`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # ORDERS
                if str(list.get()) == 'orders':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое описание:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `orders` SET `order_description`='{value1}' WHERE `order_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # PAINTS
                if str(list.get()) == 'paints':
                    id_label = Label(frame, text='Введите номер/код записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый код подтипа:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новый номер партии:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Новая дата изготовления:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    label5 = Label(frame, text='Новый цвет:')
                    label5.pack()
                    field5 = Entry(frame, bg='white')
                    field5.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())
                        value5 = str(field5.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите номер/код')
                        else:
                            if len(value1) < 1 and len(value2) < 1 and len(value3) < 1 and len(value4) < 1 and len(value5) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paints` SET `paint_name`='{value1}' WHERE `paint_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `paint_subtype_code`='{value2}' WHERE `paint_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `batch_number`='{value3}' WHERE `paint_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value4) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `date_of_manufactoring`='{value4}' WHERE `paint_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value5) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `color`='{value5}' WHERE `paint_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()

                # PAINT_SUBTYPES
                if str(list.get()) == 'paint_types':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новое описание:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новый код типа:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()
                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paint_subtypes` SET `type_name`='{value1}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paint_subtypes` SET `type_description`='{value2}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paint_subtypes` SET `paint_type_code`='{value3}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # PAINT_TYPES
                if str(list.get()) == 'paint_types':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новое описание:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paint_types` SET `type_name`='{value1}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `paint_types` SET `type_description`='{value2}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # PLANTS
                if str(list.get()) == 'plants':
                    id_label = Label(frame, text='Введите номер/код записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый адрес:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новый код страны:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Новый номер заказа:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите номер/код')
                        else:
                            if len(value1) < 1 and len(value2) < 1 and len(value3) < 1 and len(value4) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `plant_name`='{value1}' WHERE `plant_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `address`='{value2}' WHERE `plant_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `country_code`='{value3}' WHERE `plant_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value4) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `plants` SET `order_number`='{value4}' WHERE `plant_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # RESOURCES
                if str(list.get()) == 'resources':
                    id_label = Label(frame, text='Введите номер/код записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый номер склада:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новый код типа:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()

                    label4 = Label(frame, text='Новая дата изготовления:')
                    label4.pack()
                    field4 = Entry(frame, bg='white')
                    field4.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())
                        value4 = str(field4.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите номер/код')
                        else:
                            if len(value1) < 1 and len(value2) < 1 and len(value3) < 1 and len(value4) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resources` SET `resource_name`='{value1}' WHERE `resource_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resources` SET `storage_number`='{value2}' WHERE `resource_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resources` SET `type_code`='{value3}' WHERE `resource_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value4) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resources` SET `date_of_manufactoring`='{value4}' WHERE `resource_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # RESOURCE_TYPES
                if str(list.get()) == 'resource_types':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новое описание:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resource_types` SET `type_name`='{value1}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `resource_types` SET `type_description`='{value2}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # STORAGES
                if str(list.get()) == 'storages':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый адрес:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `storages` SET `storage_name`='{value1}' WHERE `storage_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `storages` SET `address`='{value2}' WHERE `storage_number`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # WORKERS
                if str(list.get()) == 'workers':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новый номер завода:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    label3 = Label(frame, text='Новый номер типа:')
                    label3.pack()
                    field3 = Entry(frame, bg='white')
                    field3.pack()


                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())
                        value3 = str(field3.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите дату')
                        else:
                            if len(value1) < 1 and len(value2) < 1 and len(value3) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `workers` SET `worker_name`='{value1}' WHERE `worker_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `workers` SET `plant_number`='{value2}' WHERE `worker_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value3) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `workers` SET `worker_type_code`='{value3}' WHERE `worker_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()
                # WORKER_TYPES
                if str(list.get()) == 'worker_types':
                    id_label = Label(frame, text='Введите код/номер записи:')
                    id_label.pack()
                    id_field = Entry(frame, bg='white')
                    id_field.pack()

                    label1 = Label(frame, text='Новое имя:')
                    label1.pack()
                    field1 = Entry(frame, bg='white')
                    field1.pack()

                    label2 = Label(frame, text='Новое описание:')
                    label2.pack()
                    field2 = Entry(frame, bg='white')
                    field2.pack()

                    def update_list():
                        id = str(id_field.get())
                        value1 = str(field1.get())
                        value2 = str(field2.get())

                        if len(id) < 1:
                            messagebox.showerror(title='Ошибка', message='Введите код/номер')
                        else:
                            if len(value1) < 1:
                                messagebox.showerror(title='Ошибка', message='Заполните одно из полей')
                            else:
                                if len(value1) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `worker_types` SET `type_name`='{value1}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                if len(value2) > 0:
                                    with connection.cursor() as cursor:
                                        update_query = f"UPDATE `worker_types` SET `type_description`='{value2}' WHERE `type_code`='{id}';"
                                        cursor.execute(update_query)
                                        connection.commit()
                                update_window.destroy()
                                refresh_page()

                    btn_update = Button(frame, text='Изменить', command=update_list)
                    btn_update.pack()

                def return_back():
                    update_window.destroy()
                    list_window.deiconify()

                btn_back = Button(frame, text='Назад', command=return_back)
                btn_back.pack()

            def delete_song():
                delete_window = Toplevel(list_window)
                list_window.withdraw()
                delete_window.geometry('450x400')
                delete_window.resizable(width=True, height=True)

                canvas = Canvas(delete_window, height=300, width=250)
                canvas.pack()

                frame = Frame(delete_window, bg='beige')
                frame.place(relwidth=1, relheight=1)

                title = Label(frame, text='Удалить запись')
                title.pack()

                id_label = Label(frame, text='Введите номер/код:')
                id_label.pack()
                id_field = Entry(frame, bg='white')
                id_field.pack()

                def on_closing():
                    delete_window.destroy()
                    list_window.deiconify()

                delete_window.protocol("WM_DELETE_WINDOW", on_closing)

                def delete_from_list():
                    id = str(id_field.get())
                    if len(id) < 1:
                        messagebox.showerror(title='Ошибка', message='Введите номер/код')
                    else:
                        with connection.cursor() as cursor:
                            if str(list.get()) == 'batches':
                                delete_query = f"DELETE FROM `batches` WHERE `batch_number` = '{id}';"
                            elif str(list.get()) == 'countries':
                                delete_query = f"DELETE FROM `countries` WHERE `country_code` = '{id}';"
                            elif str(list.get()) == 'manufactoring':
                                delete_query = f"DELETE FROM `manufactoring` WHERE `date_of_manufactoring` = '{id}';"
                            elif str(list.get()) == 'orders':
                                delete_query = f"DELETE FROM `orders` WHERE `order_number` = '{id}';"
                            elif str(list.get()) == 'paints':
                                delete_query = f"DELETE FROM `paints` WHERE `paint_number` = '{id}';"
                            elif str(list.get()) == 'paint_subtypes':
                                delete_query = f"DELETE FROM `paint_subtypes` WHERE `type_code` = '{id}';"
                            elif str(list.get()) == 'paint_types':
                                delete_query = f"DELETE FROM `paint_types` WHERE `type_code` = '{id}';"
                            elif str(list.get()) == 'plants':
                                delete_query = f"DELETE FROM `plants` WHERE `plant_number` = '{id}';"
                            elif str(list.get()) == 'resources':
                                delete_query = f"DELETE FROM `resources` WHERE `resource_code` = '{id}';"
                            elif str(list.get()) == 'resource_types':
                                delete_query = f"DELETE FROM `resource_types` WHERE `type_code` = '{id}';"
                            elif str(list.get()) == 'storages':
                                delete_query = f"DELETE FROM `storages` WHERE `storage_number` = '{id}';"
                            elif str(list.get()) == 'worker':
                                delete_query = f"DELETE FROM `storages` WHERE `worker_code` = '{id}';"
                            elif str(list.get()) == 'worker_types':
                                delete_query = f"DELETE FROM `storages` WHERE `type_code` = '{id}';"
                            cursor.execute(delete_query)
                            connection.commit()
                        delete_window.destroy()
                        refresh_page()

                btn_delete = Button(frame, text='Удалить', command=delete_from_list)
                btn_delete.pack()

                def return_back():
                    delete_window.destroy()
                    list_window.deiconify()

                btn_back = Button(frame, text='Назад', command=return_back)
                btn_back.pack()

            def dec_list():
                for widget in list_frame.winfo_children():
                    widget.destroy()
                with connection.cursor() as cursor:
                    table_name = str(list.get())
                    current_table = table_name
                    if len(table_name) < 1:
                        label = Label(list_frame, text="Пока здесь ничего нет")
                        label.pack()
                    else:
                        if current_table == 'batches':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `batch_number` DESC"
                        elif current_table == 'countries':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `country_code` DESC"
                        elif current_table == 'manufactoring':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `date_of_manufactoring` DESC"
                        elif current_table == 'orders':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `order_number` DESC"
                        elif current_table == 'paints':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `paint_number` DESC"
                        elif current_table == 'paint_subtypes':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` DESC"
                        elif current_table == 'paint_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` DESC"
                        elif current_table == 'plants':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `plant_number` DESC"
                        elif current_table == 'resources':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `resource_code` DESC"
                        elif current_table == 'resource_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` DESC"
                        elif current_table == 'storages':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `storage_number` DESC"
                        elif current_table == 'workers':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `worker_code` DESC"
                        elif current_table == 'worker_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` DESC"
                        cursor.execute(select_all_query)
                        rows = cursor.fetchall()
                        if len(rows) < 1:
                            label = Label(list_frame, text="Пока здесь ничего нет")
                            label.pack()
                        else:
                            for row in rows:
                                if current_table == 'batches':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["batch_number"]) + " Name: " + str(
                                                      row["batch_name"]) + " Plant number: " + str(row["plant_number"]))
                                    label.pack()
                                elif current_table == 'countries':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["country_code"]) + " Name: " + str(
                                                      row["country_name"]))
                                    label.pack()
                                elif current_table == 'manufactoring':
                                    label = Label(list_frame, text="Date: " + str(
                                        row["date_of_manufactoring"]) + " Produced paint: " + str(
                                        row["produced_paint"]) + " Discarded paint: " + str(
                                        row["discarded_paint"]) + " Time: " + str(row["time_for_manufactoring"]))
                                    label.pack()
                                elif current_table == 'orders':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["order_number"]) + " Description: " + str(
                                                      row["order_description"]))
                                    label.pack()
                                elif current_table == 'paints':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["paint_number"]) + " Name: " + str(
                                                      row["paint_name"]) + " Color: " + str(
                                                      row["color"]) + " Subtype code: " + str(
                                                      row["paint_subtype_code"]) + " Batch number: " + str(
                                                      row["batch_number"]) + " Date: " + str(
                                                      row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'paint_subtypes':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(
                                        row["type_description"]) + " Type code: " + str(row["paint_type_code"]))
                                    label.pack()
                                elif current_table == 'paint_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'plants':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["plant_number"]) + " Name: " + str(
                                                      row["plant_name"]) + " Address: " + str(
                                                      row["address"]) + " Country code: " + str(
                                                      row["country_code"]) + " Order num: " + str(row["order_number"]))
                                    label.pack()
                                elif current_table == 'resources':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["resource_code"]) + " Name: " + str(
                                                      row["resource_name"]) + " Storage num: " + str(
                                                      row["storage_number"]) + " Type code: " + str(
                                                      row["type_code"]) + " Date: " + str(row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'resource_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'storages':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["storage_number"]) + " Name: " + str(
                                                      row["storage_name"]) + " Address: " + str(row["address"]))
                                    label.pack()
                                elif current_table == 'workers':
                                    label = Label(list_frame, text="Code: " + str(row["worker_code"]) + " Name: " + str(
                                        row["worker_name"]) + " Plant num: " + str(
                                        row["plant_number"]) + " Type code: " + str(row["worker_type_code"]))
                                    label.pack()
                                elif current_table == 'worker_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
            def inc_list():
                for widget in list_frame.winfo_children():
                    widget.destroy()
                with connection.cursor() as cursor:
                    table_name = str(list.get())
                    current_table = table_name
                    if len(table_name) < 1:
                        label = Label(list_frame, text="Пока здесь ничего нет")
                        label.pack()
                    else:
                        if current_table == 'batches':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `batch_number` ASC"
                        elif current_table == 'countries':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `country_code` ASC"
                        elif current_table == 'manufactoring':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `date_of_manufactoring` ASC"
                        elif current_table == 'orders':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `order_number` ASC"
                        elif current_table == 'paints':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `paint_number` ASC"
                        elif current_table == 'paint_subtypes':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` ASC"
                        elif current_table == 'paint_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` ASC"
                        elif current_table == 'plants':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `plant_number` ASC"
                        elif current_table == 'resources':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `resource_code` ASC"
                        elif current_table == 'resource_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` ASC"
                        elif current_table == 'storages':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `storage_number` ASC"
                        elif current_table == 'workers':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `worker_code` ASC"
                        elif current_table == 'worker_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_code` ASC"
                        cursor.execute(select_all_query)
                        rows = cursor.fetchall()
                        if len(rows) < 1:
                            label = Label(list_frame, text="Пока здесь ничего нет")
                            label.pack()
                        else:
                            for row in rows:
                                if current_table == 'batches':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["batch_number"]) + " Name: " + str(
                                                      row["batch_name"]) + " Plant number: " + str(row["plant_number"]))
                                    label.pack()
                                elif current_table == 'countries':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["country_code"]) + " Name: " + str(
                                                      row["country_name"]))
                                    label.pack()
                                elif current_table == 'manufactoring':
                                    label = Label(list_frame, text="Date: " + str(
                                        row["date_of_manufactoring"]) + " Produced paint: " + str(
                                        row["produced_paint"]) + " Discarded paint: " + str(
                                        row["discarded_paint"]) + " Time: " + str(row["time_for_manufactoring"]))
                                    label.pack()
                                elif current_table == 'orders':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["order_number"]) + " Description: " + str(
                                                      row["order_description"]))
                                    label.pack()
                                elif current_table == 'paints':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["paint_number"]) + " Name: " + str(
                                                      row["paint_name"]) + " Color: " + str(
                                                      row["color"]) + " Subtype code: " + str(
                                                      row["paint_subtype_code"]) + " Batch number: " + str(
                                                      row["batch_number"]) + " Date: " + str(
                                                      row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'paint_subtypes':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(
                                        row["type_description"]) + " Type code: " + str(row["paint_type_code"]))
                                    label.pack()
                                elif current_table == 'paint_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'plants':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["plant_number"]) + " Name: " + str(
                                                      row["plant_name"]) + " Address: " + str(
                                                      row["address"]) + " Country code: " + str(
                                                      row["country_code"]) + " Order num: " + str(row["order_number"]))
                                    label.pack()
                                elif current_table == 'resources':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["resource_code"]) + " Name: " + str(
                                                      row["resource_name"]) + " Storage num: " + str(
                                                      row["storage_number"]) + " Type code: " + str(
                                                      row["type_code"]) + " Date: " + str(row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'resource_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'storages':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["storage_number"]) + " Name: " + str(
                                                      row["storage_name"]) + " Address: " + str(row["address"]))
                                    label.pack()
                                elif current_table == 'workers':
                                    label = Label(list_frame, text="Code: " + str(row["worker_code"]) + " Name: " + str(
                                        row["worker_name"]) + " Plant num: " + str(
                                        row["plant_number"]) + " Type code: " + str(row["worker_type_code"]))
                                    label.pack()
                                elif current_table == 'worker_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
            def inc_name_list():
                for widget in list_frame.winfo_children():
                    widget.destroy()
                with connection.cursor() as cursor:
                    table_name = str(list.get())
                    current_table = table_name
                    if len(table_name) < 1:
                        label = Label(list_frame, text="Пока здесь ничего нет")
                        label.pack()
                    else:
                        if current_table == 'batches':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `batch_name` ASC"
                        elif current_table == 'countries':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `country_name` ASC"
                        elif current_table == 'manufactoring':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `produced_paint` ASC"
                        elif current_table == 'orders':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `order_description` ASC"
                        elif current_table == 'paints':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `paint_name` ASC"
                        elif current_table == 'paint_subtypes':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_name` ASC"
                        elif current_table == 'paint_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_name` ASC"
                        elif current_table == 'plants':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `plant_name` ASC"
                        elif current_table == 'resources':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `resource_name` ASC"
                        elif current_table == 'resource_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_name` ASC"
                        elif current_table == 'storages':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `storage_name` ASC"
                        elif current_table == 'workers':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `worker_name` ASC"
                        elif current_table == 'worker_types':
                            select_all_query = f"SELECT * FROM `{table_name}` ORDER BY `type_name` ASC"
                        cursor.execute(select_all_query)
                        rows = cursor.fetchall()
                        if len(rows) < 1:
                            label = Label(list_frame, text="Пока здесь ничего нет")
                            label.pack()
                        else:
                            for row in rows:
                                if current_table == 'batches':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["batch_number"]) + " Name: " + str(
                                                      row["batch_name"]) + " Plant number: " + str(row["plant_number"]))
                                    label.pack()
                                elif current_table == 'countries':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["country_code"]) + " Name: " + str(
                                                      row["country_name"]))
                                    label.pack()
                                elif current_table == 'manufactoring':
                                    label = Label(list_frame, text="Date: " + str(
                                        row["date_of_manufactoring"]) + " Produced paint: " + str(
                                        row["produced_paint"]) + " Discarded paint: " + str(
                                        row["discarded_paint"]) + " Time: " + str(row["time_for_manufactoring"]))
                                    label.pack()
                                elif current_table == 'orders':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["order_number"]) + " Description: " + str(
                                                      row["order_description"]))
                                    label.pack()
                                elif current_table == 'paints':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["paint_number"]) + " Name: " + str(
                                                      row["paint_name"]) + " Color: " + str(
                                                      row["color"]) + " Subtype code: " + str(
                                                      row["paint_subtype_code"]) + " Batch number: " + str(
                                                      row["batch_number"]) + " Date: " + str(
                                                      row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'paint_subtypes':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(
                                        row["type_description"]) + " Type code: " + str(row["paint_type_code"]))
                                    label.pack()
                                elif current_table == 'paint_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'plants':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["plant_number"]) + " Name: " + str(
                                                      row["plant_name"]) + " Address: " + str(
                                                      row["address"]) + " Country code: " + str(
                                                      row["country_code"]) + " Order num: " + str(row["order_number"]))
                                    label.pack()
                                elif current_table == 'resources':
                                    label = Label(list_frame,
                                                  text="Code: " + str(row["resource_code"]) + " Name: " + str(
                                                      row["resource_name"]) + " Storage num: " + str(
                                                      row["storage_number"]) + " Type code: " + str(
                                                      row["type_code"]) + " Date: " + str(row["date_of_manufactoring"]))
                                    label.pack()
                                elif current_table == 'resource_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()
                                elif current_table == 'storages':
                                    label = Label(list_frame,
                                                  text="Number: " + str(row["storage_number"]) + " Name: " + str(
                                                      row["storage_name"]) + " Address: " + str(row["address"]))
                                    label.pack()
                                elif current_table == 'workers':
                                    label = Label(list_frame, text="Code: " + str(row["worker_code"]) + " Name: " + str(
                                        row["worker_name"]) + " Plant num: " + str(
                                        row["plant_number"]) + " Type code: " + str(row["worker_type_code"]))
                                    label.pack()
                                elif current_table == 'worker_types':
                                    label = Label(list_frame, text="Code: " + str(row["type_code"]) + " Name: " + str(
                                        row["type_name"]) + " Description: " + str(row["type_description"]))
                                    label.pack()

            def search_list():
                search_window = Toplevel(list_window)
                list_window.withdraw()
                search_window.geometry('450x400')
                search_window.resizable(width=True, height=True)

                canvas = Canvas(search_window, height=300, width=250)
                canvas.pack()

                frame = Frame(search_window, bg='beige')
                frame.place(relwidth=1, relheight=1)

                title = Label(frame, text='Поиск по списку')
                title.pack()

                search_field = Entry(frame, bg='white')
                search_field.pack()

                search_list_frame = Frame(frame, bg='white')
                search_list_frame.pack()

                hint = Label(search_list_frame, text='Найденные совпадения:')
                hint.pack()

                def on_closing():
                    search_window.destroy()
                    list_window.deiconify()

                search_window.protocol("WM_DELETE_WINDOW", on_closing)

                def search_in_list():
                    for widget in search_list_frame.winfo_children():
                        widget.destroy()
                    table_name = str(list.get())
                    current_table = table_name
                    search = str(search_field.get())
                    if len(search) < 1:
                        messagebox.showerror(title='Ошибка', message='Поле не может быть пустым')
                    else:
                        with connection.cursor() as cursor:
                            if current_table == 'batches':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `batch_number` LIKE '%{search}%' OR `batch_name` LIKE '%{search}%' OR `plant_number` LIKE '%{search}%'"
                            elif current_table == 'countries':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `country_code` LIKE '%{search}%' OR `country_name` LIKE '%{search}%'"
                            elif current_table == 'manufactoring':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `date_of_manufactoring` LIKE '%{search}%' OR `produced_paint` LIKE '%{search}%' OR `discarded_paint` LIKE '%{search}%' OR `time_for_manufactoring` LIKE '%{search}%'"
                            elif current_table == 'orders':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `order_number` LIKE '%{search}%' OR `order_description` LIKE '%{search}%'"
                            elif current_table == 'paints':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `paint_number` LIKE '%{search}%' OR `paint_name` LIKE '%{search}%' OR `paint_subtype_code` LIKE '%{search}%' OR `batch_number` LIKE '%{search}%' OR `date_of_manufactoring` LIKE '%{search}%' OR `color` LIKE '%{search}%'"
                            elif current_table == 'paint_types':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `type_code` LIKE '%{search}%' OR `type_name` LIKE '%{search}%' OR `type_description` LIKE '%{search}%'"
                            elif current_table == 'paint_subtypes':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `type_code` LIKE '%{search}%' OR `type_name` LIKE '%{search}%' OR `type_description` LIKE '%{search}%' OR `paint_type_code` LIKE '%{search}%'"
                            elif current_table == 'plants':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `plant_number` LIKE '%{search}%' OR `plant_name` LIKE '%{search}%' OR `address` LIKE '%{search}%' OR `country_code` LIKE '%{search}%' OR `order_number` LIKE '%{search}%'"
                            elif current_table == 'resources':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `resource_code` LIKE '%{search}%' OR `resource_name` LIKE '%{search}%' OR `storage_number` LIKE '%{search}%' OR `type_code` LIKE '%{search}%' OR `date_of_manufactoring` LIKE '%{search}%'"
                            elif current_table == 'resource_types':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `type_code` LIKE '%{search}%' OR `type_name` LIKE '%{search}%' OR `type_description` LIKE '%{search}%'"
                            elif current_table == 'storages':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `storage_number` LIKE '%{search}%' OR `storage_name` LIKE '%{search}%' OR `address` LIKE '%{search}%'"
                            elif current_table == 'workers':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `worker_code` LIKE '%{search}%' OR `worker_name` LIKE '%{search}%' OR `plant_number` LIKE '%{search}%' OR `worker_type_code` LIKE '%{search}%'"
                            elif current_table == 'worker_types':
                                select_query = f"SELECT * FROM `{current_table}` WHERE `type_code` LIKE '%{search}%' OR `type_name` LIKE '%{search}%' OR `type_description` LIKE '%{search}%'"
                            cursor.execute(select_query)
                            rows = cursor.fetchall()
                            if len(rows) < 1:
                                label = Label(search_list_frame, text="Пока здесь ничего нет")
                                label.pack()
                            else:
                                for row in rows:
                                    if current_table == 'batches':
                                        label = Label(search_list_frame,
                                                      text="Number: " + str(row["batch_number"]) + " Name: " + str(
                                                          row["batch_name"]) + " Plant number: " + str(
                                                          row["plant_number"]))
                                        label.pack()
                                    elif current_table == 'countries':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["country_code"]) + " Name: " + str(
                                                          row["country_name"]))
                                        label.pack()
                                    elif current_table == 'manufactoring':
                                        label = Label(search_list_frame, text="Date: " + str(
                                            row["date_of_manufactoring"]) + " Produced paint: " + str(
                                            row["produced_paint"]) + " Discarded paint: " + str(
                                            row["discarded_paint"]) + " Time: " + str(row["time_for_manufactoring"]))
                                        label.pack()
                                    elif current_table == 'orders':
                                        label = Label(search_list_frame,
                                                      text="Number: " + str(
                                                          row["order_number"]) + " Description: " + str(
                                                          row["order_description"]))
                                        label.pack()
                                    elif current_table == 'paints':
                                        label = Label(search_list_frame,
                                                      text="Number: " + str(row["paint_number"]) + " Name: " + str(
                                                          row["paint_name"]) + " Color: " + str(
                                                          row["color"]) + " Subtype code: " + str(
                                                          row["paint_subtype_code"]) + " Batch number: " + str(
                                                          row["batch_number"]) + " Date: " + str(
                                                          row["date_of_manufactoring"]))
                                        label.pack()
                                    elif current_table == 'paint_subtypes':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["type_code"]) + " Name: " + str(
                                                          row["type_name"]) + " Description: " + str(
                                                          row["type_description"]) + " Type code: " + str(
                                                          row["paint_type_code"]))
                                        label.pack()
                                    elif current_table == 'paint_types':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["type_code"]) + " Name: " + str(
                                                          row["type_name"]) + " Description: " + str(
                                                          row["type_description"]))
                                        label.pack()
                                    elif current_table == 'plants':
                                        label = Label(search_list_frame,
                                                      text="Number: " + str(row["plant_number"]) + " Name: " + str(
                                                          row["plant_name"]) + " Address: " + str(
                                                          row["address"]) + " Country code: " + str(
                                                          row["country_code"]) + " Order num: " + str(
                                                          row["order_number"]))
                                        label.pack()
                                    elif current_table == 'resources':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["resource_code"]) + " Name: " + str(
                                                          row["resource_name"]) + " Storage num: " + str(
                                                          row["storage_number"]) + " Type code: " + str(
                                                          row["type_code"]) + " Date: " + str(
                                                          row["date_of_manufactoring"]))
                                        label.pack()
                                    elif current_table == 'resource_types':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["type_code"]) + " Name: " + str(
                                                          row["type_name"]) + " Description: " + str(
                                                          row["type_description"]))
                                        label.pack()
                                    elif current_table == 'storages':
                                        label = Label(search_list_frame,
                                                      text="Number: " + str(row["storage_number"]) + " Name: " + str(
                                                          row["storage_name"]) + " Address: " + str(row["address"]))
                                        label.pack()
                                    elif current_table == 'workers':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["worker_code"]) + " Name: " + str(
                                                          row["worker_name"]) + " Plant num: " + str(
                                                          row["plant_number"]) + " Type code: " + str(
                                                          row["worker_type_code"]))
                                        label.pack()
                                    elif current_table == 'worker_types':
                                        label = Label(search_list_frame,
                                                      text="Code: " + str(row["type_code"]) + " Name: " + str(
                                                          row["type_name"]) + " Description: " + str(
                                                          row["type_description"]))
                                        label.pack()
                btn_delete = Button(frame, text='Поиск', command=search_in_list)
                btn_delete.pack()

                def return_back():
                    search_window.destroy()
                    list_window.deiconify()

                btn_back = Button(frame, text='Назад', command=return_back)
                btn_back.pack()

            def quit_list():
                list_window.destroy()
                root.deiconify()

            # BUTTON ADD
            btn_add = Button(frame, text='Добавить', command=add_record)
            btn_add.pack()

            # BUTTON UPDATE
            btn_update = Button(frame, text='Изменить', command=update_song)
            btn_update.pack()
            #
            # BUTTON DELETE
            btn_delete = Button(frame, text='Удалить', command=delete_song)
            btn_delete.pack()

            # BUTTON REFRESH
            btn_refresh = Button(frame, text='Обновить', command=refresh_page)
            btn_refresh.pack()

            # BUTTON DEC
            btn_dec = Button(frame, text='Сортировать по убыванию', command=dec_list)
            btn_dec.pack()
            # BUTTON DEC
            btn_inc = Button(frame, text='Сортировать по возрастанию', command=inc_list)
            btn_inc.pack()
            # BUTTON INC
            btn_inc_name = Button(frame, text='Сортировать по имени', command=inc_name_list)
            btn_inc_name.pack()

            # BUTTON SEARCH
            btn_search = Button(frame, text='Поиск...', command=search_list)
            btn_search.pack()

            # BUTTON QUIT
            btn_quit = Button(frame, text='Выйти', command=quit_list)
            btn_quit.pack()


        def add_user(login, password, sign_up_window):
            with connection.cursor() as cursor:
                search_query = f"SELECT * FROM `users` WHERE `login`='{login}'"
                cursor.execute(search_query)
                rows = cursor.fetchall()
                if len(rows) < 1:
                    insert_query = f"INSERT INTO `users` (login, password) VALUES ('{login}','{password}');"
                    cursor.execute(insert_query)
                    connection.commit()
                    messagebox.showinfo(title='Название', message='Успешная регистрация')
                    sign_up_window.destroy()
                    root.deiconify()
                else:
                    messagebox.showerror(title='Ошибка', message='Пользователь с таким логином уже существует')


        def search_user(login, password):
            with connection.cursor() as cursor:
                search_query = f"SELECT * FROM `users` WHERE `login`='{login}' AND `password`='{password}'"
                cursor.execute(search_query)
                rows = cursor.fetchall()
                if len(rows) < 1:
                    messagebox.showerror(title='Ошибка', message='Такого пользователя не найдено')
                else:
                    create_list()

        root = Tk()
        list = root

        def sign_in():
            login = str(login_field.get())
            password = str(pass_field.get())

            if len(login) < 1 or len(password) < 1:
                messagebox.showerror(title='Ошибка', message='Заполните все поля')
            else:
                search_user(login, password)


        def sign_up():
            sign_up_window = Toplevel(root)
            root.withdraw()
            sign_up_window.geometry('450x400')
            sign_up_window.resizable(width=True, height=True)

            canvas = Canvas(sign_up_window, height=300, width=250)
            canvas.pack()

            frame = Frame(sign_up_window, bg='beige')
            frame.place(relwidth=1, relheight=1)

            title = Label(frame, text='Зарегистрируйтесь в системе')
            title.pack()

            login_label = Label(frame, text='Логин:')
            login_label.pack()
            login_field_reg = Entry(frame, bg='white')
            login_field_reg.pack()

            pass_label = Label(frame, text='Пароль:')
            pass_label.pack()
            pass_field_reg = Entry(frame, bg='white', show='*')
            pass_field_reg.pack()

            def on_closing():
                sign_up_window.destroy()
                root.deiconify()

            sign_up_window.protocol("WM_DELETE_WINDOW", on_closing)

            def user_register():
                login = str(login_field_reg.get())
                password = str(pass_field_reg.get())

                if len(login) < 1 or len(password) < 1:
                    messagebox.showerror(title='Ошибка', message='Заполните все поля')
                else:
                    add_user(login, password, sign_up_window)

            btn_sign_up = Button(frame, text='Зарегистрироваться', command=user_register)
            btn_sign_up.pack()

            def return_back():
                sign_up_window.destroy()
                root.deiconify()

            btn_back = Button(frame, text='Назад', command=return_back)
            btn_back.pack()

            sign_up_window.mainloop()
            # root.deiconify()

        root.title('Paint Manufactoring')
        root.geometry('450x400')
        root.resizable(width=True, height=True)

        canvas = Canvas(root, height=300, width=250)
        canvas.pack()

        frame = Frame(root, bg='beige')
        frame.place(relwidth=1, relheight=1)

        title = Label(frame, text='Для продолжения необходимо авторизоваться', font='Times 14')
        title.pack()

        login_label = Label(frame, text='Логин:')
        login_label.pack()
        login_field = Entry(frame, bg='white')
        login_field.pack()

        pass_label = Label(frame, text='Пароль:')
        pass_label.pack()
        pass_field = Entry(frame, bg='white', show='*')
        pass_field.pack()

        btn_sign_in = Button(frame, text='Войти', command=sign_in)
        btn_sign_in.pack()

        btn_sign_up = Button(frame, text='Зарегистрироваться', command=sign_up)
        btn_sign_up.pack()

        root.mainloop()

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused")
    print(ex)


