def solution(phone_number):
    a = len(phone_number)
    front = len(phone_number[:a-4]) * '*'
    rear = phone_number[a-4:]
    return front+rear