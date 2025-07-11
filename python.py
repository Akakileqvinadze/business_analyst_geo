import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env ფაილიდან API გასაღების ჩატვირთვა
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # ⚠️ უნდა გეწეროს GEMINI_API_KEY .env-ში


def analyze_business_idea(idea_text):
    prompt = f"""
გაანალიზე შემდეგი ბიზნეს იდეა:

{idea_text}

და შეაფასე შემდეგი პუნქტებით:
1. იდეის მოკლე რეზიუმე
2. მიზნობრივი აუდიტორია
3. მონეტიზაციის გზები
4. ანალოგიური პროდუქტები ან კონკურენტები (თუ იცი)
5. იდეის სიძლიერეები და სუსტი მხარეები
6. გრძელვადიანი მდგრადობის პროგნოზი
7. რეკომენდაცია იდეის გაუმჯობესებისთვის
    """

    model = genai.GenerativeModel("gemini-1.5-flash")  # ან გამოიყენე "gemini-1.5-pro", თუ საჭიროა
    response = model.generate_content(prompt)

    return response.text


def main():
    idea_text = input("შეიყვანე ბიზნეს იდეა ქართულად: ")
    result = analyze_business_idea(idea_text)
    print("\n🔍 ანალიზის შედეგი:\n")
    print(result)


if __name__ == "__main__":
    main()
