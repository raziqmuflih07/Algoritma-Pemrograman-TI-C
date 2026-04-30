print("=" *13)
print("1. RADIX SORT")
print("=" *13)

data1 = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print("\ndata sebelum di sorting menggunakan Radix sort ==> ", data1)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(data1)
exp = 1

while maxVal // exp > 0:

  while len(data1) > 0:
    val = data1.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      data1.append(val)

  exp *= 10

print("\ndata setelah di sorting menggunakan Radix sort ==> ", data1)

print("\n" + "=" *13)
print("2. MERGE SORT")
print("=" *13)

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

data2 = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print("\ndata sebelum disorting menggunakan Merge sort ==> ",data2)

data_merge = mergeSort(data2)
print("\ndata setelah disorting menggunakan Merge sort ==> ", data_merge)  

print("\n" + "=" *32)
print(" Binary search dan Linear search ")
print("=" *32)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]  # Mengembalikan index dan value
    return None, None

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, None

data3 = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

try:
    cari_angka = int(input("masukkan angka yang ingin dicari : "))

    index1, nilai1 = linear_search(data_merge, cari_angka)
    print(f"\n[HASIL LINEAR SEARCH]")
    if index1 is not None:
        print(f"Ditemukan! Index: {index1}, nilai: {nilai1}")
    else:
        print("tidak ada")

    # 2. Eksekusi Binary Search
    index2, nilai2 = binary_search(data_merge, cari_angka)
    print(f"\n[HASIL BINARY SEARCH]")
    if index2 is not None:
        print(f"Ditemukan! Index: {index2}, nilai: {nilai2}")
    else:
        print("tidak ada")

except ValueError:
    print("\nInput salah! hanya menerima input angka.")