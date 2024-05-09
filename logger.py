import datetime


def write_log(instance, is_update=False):
    with open('logs/student_data.txt', 'a') as file:
        file.write('\n************************************************')
        file.write(f"\n {'Updated Log:' if is_update else 'სტუდენტის ID:'} \t\t {instance.student_id.get()}")
        if is_update:
            file.write(f"\n სტუდენტის ID: \t {instance.student_id.get()}")
        file.write(f"\n სტუდენტის სახელი: \t {instance.saxeli.get()}")
        file.write(f"\n სტუდენტი: \t {instance.saxeli.get()} {instance.gvari.get()}")
        file.write(f"\n კურსის სახელი: \t {instance.kursis_saxeli.get()}")
        file.write(f"\n Python: \t {instance.python.get()}")
        file.write(f"\n C#: \t {instance.csharp.get()}")
        file.write(f"\n Java: \t {instance.java.get()}")
        file.write(f"\n JavaScript: \t {instance.javascript.get()}")
        file.write(f"\n C++: \t {instance.cplusplus.get()}")
        file.write(f"\n ინფორმაციული უსაფრთხოება: \t {instance.inf_usf.get()}")
        file.write(f"\n ქსელები: \t {instance.qselebi.get()}")
        file.write(f"\n სტატუსი: \t {instance.statusi.get()}")
        file.write('\n\n================================')
        file.write(f"\n ქულათა ჯამი: \t {instance.qulata_jami.get()}")
        file.write(f"\n ქულათა პროცენტი: \t {instance.procenti.get()}")
        file.write('\n================================')
        file.write(f"\n{'Create Date' if not is_update else 'Update Date'}: {datetime.datetime.now()}\n")
        file.write('\n************************************************')



