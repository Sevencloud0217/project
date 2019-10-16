


class Pager:
    """
    flask 通过limit offset 对数据进行分页
    切片
    提供的功能
    """
    def __init__(self,data,page_size):
        """

        :param data: 数据
        :param page_size:  每页条数
        """
        self.data = data
        self.page_size = page_size
        self.is_start = False
        self.is_end = False
        self.page_count = len(data)  #总条数
        self.next_page = 0 #下一页
        self.previous_page = 0 #上一页
        self.page_number = self.page_count /self.page_size #总的页数
        if self.page_number == int(self.page_number):
            self.page_number = int(self.page_number)
        else:
            self.page_number = int(self.page_number) +1

        self.page_range = (x for x in range(1,self.page_number+1))
    def page_data(self,page):
        """
        :return: 分页的数据
        """
        page_start = (page-1) * self.page_size #切片开始的位置
        page_end = page * self.page_size #结束的位置
        result = self.data[page_start:page_end]
        if page == 1:
            self.is_start = True
        if page == self.page_number:
            self.is_end = True

        self.next_page = page + 1 #上一页
        self.previous_page = page -1  #下一页
        return result

from model import User,Leave
def add_data():
    for x in range(100):
        leave = Leave()
        leave.request_id = 1
        leave.request_name = "小柒"
        leave.request_type= "病假"
        leave.request_start = "2019-10-16"
        leave.request_end = "2019-10-20"
        leave.request_number= 4
        leave.request_phone = "12345678909"
        leave.request_status = 0
        leave.save()
if __name__ == '__main__':
    while True:
        page = int(input(">>>"))
        params = Leave.query.all()
        pager = Pager(params,10)
        result = pager.page_data(page)
        print(result)
        print(pager.page_size)
        print(pager.page_number)
        print(list(pager.page_range))
        print(pager.page_count)
        print(pager.is_start)
        print(pager.is_end)
        print(pager.next_page)
        print(pager.previous_page)
    # add_data()
