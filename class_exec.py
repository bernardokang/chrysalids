from time import ctime

class MyHome:
    #얘들은 클래쓰변수
    #이 클래스 변수를 불러서 바로 고칠수는 없고, 펑션을 매개로 해서 값을 바꿔줄 수 있다는!
    #instance.paintRoof('yellow')이런 식으로 기본 클래스변수를 바꿔주는 것이지!
    colorRoof = 'red'
    stateDoor = 'closed'

    #멤버펑션
    def paintRoof(self, color):
        #셀프변수
        self.colorRoof = color
    def openDoor(self):
        self.stateDoor = 'open'
    def closeDoor(self):
        self.stateDoor = 'close'
    def printStatus(self):
        print("Roof color is", self.colorRoof,
        "and Door is", self.stateDoor)

    #이닛 컨스트럭터
    def __init__(self, SetAddress):
        print("Build on", SetAddress)
        print("Build at",ctime())

    #디스트럭터 = 정리문구(끝났을 때 출력), 얘는 셀프만 받는다 뭘 더 받지 않는다
    def __del__(self):
        print("Destroyed at", ctime())




homeAtDaejeon = MyHome("kaist")
#이것들은 사실 컨스트럭터를 콜하는 함수다: 원하는 초기값을 원하는 형태로 값을 저장해놓고 시작하기
#이닛 컨스트럭터에서 셀프는 존재하지 않는다(특이하다, 예정표만을 나타내는 셀프인듯)

homeAtSeoul = MyHome("snu")
homeAtSeoul.openDoor()
homeAtLondon = MyHome("londonuinv")


#클래스의 변수만 호출도 가능하다
print(homeAtLondon.colorRoof)


homeAtDaejeon.paintRoof('blue')
homeAtDaejeon.printStatus()
homeAtSeoul.printStatus()
