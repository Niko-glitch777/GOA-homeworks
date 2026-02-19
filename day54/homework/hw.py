# 1)კვადრატი: შექმენი lambda, რომელიც რიცხვს აიყვანს კვადრატში.

square = lambda x: x ** 2
# 2)გამრავლება: შექმენი lambda, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ნამრავლს.

multiply = lambda x, y: x * y

# 3)ტემპერატურა: დაწერე lambda, რომელიც ცელსიუსს გადაიყვანს ფარენჰეიტში ფორმულით:F = C * 1.8 + 32

celsus = lambda c: c * 1.8 + 32
# 4)ლუწი/კენტი: შექმენი lambda, რომელიც აბრუნებს True-ს, თუ რიცხვი ლუწია და False-ს, თუ კენტია.


# 5)სტრიქონის სიგრძე: შექმენი lambda, რომელიც აბრუნებს ტექსტის სიგრძეს.

length = lambda string: len(string)
# 6)სახელების დალაგება: გაქვს სია ["დათო", "ეკა", "ალექსანდრე", "გია"]. დაალაგე სახელები მათი სიგრძის მიხედვით.

name_sort = sorted(key=lambda name: len(name))
# 7)ბოლო ასო: იგივე სია დაალაგე სახელების ბოლო ასოს მიხედვით.

name_sort2 = sorted(key=lambda name1: name1[-1])
# 8)კოორდინატები: გაქვს წერტილების სია: [(1, 5), (8, 2), (4, 10)]. დაალაგე ისინი მეორე (Y) კოორდინატის მიხედვით.

lst_sort = sorted(key=lambda Y: Y[1])
# 9) გაქვს პროდუქტების კოლექცია: [{"name": "პური", "price": 1.2}, {"name": "რძე", "price": 4.5}, {"name": "ყველი", "price": 12.0}]. დაალაგე ისინი ფასის მიხედვით ზრდადობით.

proce_sort = sorted(key=lambda price_sort: price_sort["price"])

# 10)Case-Insensitive: დაალაგე სია ["banana", "Apple", "cherry", "Berry"] ისე, რომ დიდმა და პატარა ასოებმა გავლენა არ მოახდინოს ანბანურ თანმიმდევრობაზე (მინიშნება: .lower()).

Case = sorted(key=lambda case: case.lower())

# 11)ასაკის კონტროლი: შექმენი lambda, რომელიც იღებს ასაკს და აბრუნებს "Adult"-ს, თუ ასაკი 18 ან მეტია, და "Minor"-ს სხვა შემთხვევაში.

age= lambda age: "Adult" if age >= 18 else "Minor"

# 12)დადებითი/უარყოფითი: შექმენი lambda, რომელიც რიცხვის მიღებისას აბრუნებს "Positive", "Negative" ან "Zero".

negative_positivve = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
# გამოიყენეთ სინტაქსი: lambda x: "კი" if პირობა else "არა"

