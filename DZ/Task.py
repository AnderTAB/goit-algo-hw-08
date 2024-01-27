import heapq

def minimize_cost(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0
    
    while len(cable_lengths) > 1:

        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        combined_length = cable1 + cable2
        total_cost += combined_length
        print(f"Проміжні результати:\nдовжини дротів що є {cable_lengths}, об'єднаний дрід - {combined_length}")
        heapq.heappush(cable_lengths, combined_length)

    return combined_length

if __name__ =="__main__":
    cable_lengths = [4, 2, 7, 6, 1]
    result = minimize_cost(cable_lengths)
    print("Мінімальні загальні витрати:", result)