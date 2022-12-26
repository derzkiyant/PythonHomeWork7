import view
import read
import write


def button_click():
    lister1 = view.view_input1()
    if lister1 == '0':
        lister2 = view.view_input2()
        if lister2 == '0':
            writer = write.write1()
            view.view_write(writer)
        elif lister2 == '1':
            writer = write.write2()
            view.view_write(writer)
    elif lister1 == '1':
        lister2 = view.view_input2()
        if lister2 == '0':
            reader = read.read1()
            view.view_read(reader[0], reader[1])
        elif lister2 == '1':
            reader = read.read2()
            view.view_read(reader[0], reader[1])
