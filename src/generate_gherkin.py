from model.ai_model import generate_gherkin_from_requirements

def main():
    with open("data/requirements.txt", "r") as req_file:
        requirements = req_file.readlines()
    gherkin = generate_gherkin_from_requirements(requirements)
    with open("features/generated.feature", "w") as out_file:
        out_file.write(gherkin)
    print("Gherkin scenarios generated in features/generated.feature")

if __name__ == "__main__":
    main()