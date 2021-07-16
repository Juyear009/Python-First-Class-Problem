class Book():  # 추상클래스
    def get_rental_price(self, day):
        pass


class ComicBook(Book):  # 만화책 대여비용을 계산해주는 클래스
    def get_rental_price(self, day):
        cost = 500
        day -= 2
        cost2 = 200 * day
        return cost + cost2


class Novel(Book):  # 소설책 대여비용을 계산해주는 클래스
    def get_rental_price(self, day):
        cost = 1000
        day -= 3
        cost2 = 300 * day
        return cost + cost2


def solution(booklist, day):
    books = []
    total = 0
    for i in range(len(booklist)):
        if booklist[i] == 'comic':
            books.append(ComicBook())
        elif booklist[i] == 'novel':
            books.append(Novel())

    for x in books:
        total += x.get_rental_price(day)
    return total


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
book_types = ["comic", "comic", "novel"]
day = 4
ret = solution(book_types, day)
print("solution 함수의 반환 값은", ret, "입니다.")
