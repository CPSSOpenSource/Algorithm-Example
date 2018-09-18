class LinkedList:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data
    
    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data
    
    def set_next(self, next):
        self._next = next

# LinkedList형을 가진 인스턴스를 만들어 각각의 변수에 대입합니다.
data_one = LinkedList(1)
data_two = LinkedList(2)
data_three = LinkedList(3)

# 만든 변수들을 list에 담습니다.
data_list = [data_one, data_two, data_three]

# iterable형을 가지는 data_list 변수에서 데이터를 한개씩 꺼내옵니다.
for a in data_list:
    if len(data_list) - 1 != data_list.index(a):
        a.set_next(data_list[data_list.index(a) + 1])

for index, a in enumerate(data_list):
    print("%d번째 링크드 리스트 정보" % index)
    print("data: {data}, 이것의 객체아이디(주소): {id}, 연결된 다음 객체주소(주소): {next_id}\n".format(data=a.get_data(), id=id(a), next_id=id(a.get_next())))
