from model import *
import datetime

# Get Bag of Words from giving string
def get_bag_of_words(a):
  """
  Fungsi untuk mendapatkan kumpulan kata-kata 
  berbentuk array dari input string yang dimasukkan.
  """
  a = remove_punc(a)
  b = nltk.word_tokenize(a)
  b = [stemmer.stem(word.lower()) for word in b]
  bag = []
  for w in words:
    bag.append(1 if w in b else 0)
  return np.array(bag)

# Classify string by tag
def classify(a):
  """
  Fungsi untuk mengklasifikasikan jenis intent user 
  menggunakan model ANN yang sudah dibuat sebelumnya.
  """
  bag = get_bag_of_words(a)
  pred = model.predict(bag.reshape(1, 202, 1))
  max = [0, 0]
  for i in range(pred.shape[1]):
    if max[0] < pred[0][i]:
      max[0] = pred[0][i]
      max[1] = i
  return classes[max[1]], max[0]

# Generate response for given tag
def response(class_name):
  """
  Fungsi untuk menghasilkan respond berdasarkan 
  intent dari model ANN yang sudah dibuat.
  """
  for intent in intents:
    if intent["tag"] == class_name:
      responses = intent["responses"]
      return responses[random.randint(1, len(responses)) - 1]

# Classify and response for given query
def classify_and_response(a):
  """
  Fungsi untuk menampilkan respond, jenis intent dan akurasi model.
  """
  classify_ = classify(a)
  class_name = classify_[0]

  now = datetime.datetime.now()
  hour = now.hour

  if hour < 12 and classify_[0] == "greeting":
    respond = f"Respond : Halo selamat pagi, {response(class_name)}\nTipe intent : {classify_[0]}\nAkurasi : {classify_[1]}"
  elif hour < 18 and classify_[0] == "greeting":
    respond = f"Respond : Halo selamat siang, {response(class_name)}\nTipe intent : {classify_[0]}\nAkurasi : {classify_[1]}"
  elif hour > 18 and classify_[0] == "greeting":
    respond = f"Respond : Halo selamat malam, {response(class_name)}\nTipe intent : {classify_[0]}\nAkurasi : {classify_[1]}"
  else:
    respond = f"Respond : {response(class_name)}\nTipe intent : {classify_[0]}\nAkurasi : {classify_[1]}"
    
  return respond

if __name__ == "__main__":
  print(f"{10*'-'}Program Chatbot Toko Online{10*'-'}")
  while True:
    chat = str(input("Chat: "))
    if chat == "exit":
      break
    print(classify_and_response(chat))
    print(f"\nKetik 'exit' untuk keluar... \n{30*'-'}")
    