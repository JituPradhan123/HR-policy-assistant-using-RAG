from hr_assistant.pipeline import ask, build_hr_assistant

def main():
    print("Building the HR policy assistant...")
    agent = build_hr_assistant()
    print("Assistant ready!\n")
    
    demo_questions = [
        "Can i work from home everyday?"
    ]
    
    for question in demo_questions:
        print("="*70)
        print("QUESTION:",question)
        print("-"*70)
        answer = ask(agent,question)
        print("ANSWER:",answer)
        print("="*70)
        print()

if __name__=="__main__":
    main()