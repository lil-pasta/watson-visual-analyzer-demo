import sys, json, os
from watson_developer_cloud import VisualRecognitionV3

menu_options = {}
files = ()

#get a JSON with all classifiers
def get_classifiers():
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        api_key='9769d7adc1619cfc330d6e5e869ff3893bcf64fd')
    classifiers = visual_recognition.list_classifiers(verbose=True)
    class_ids = json.dumps(classifiers, indent=2)
    return classifiers


#function used to ask Watson Visual Recognition to check on an image
def classify_image():
    visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='9769d7adc1619cfc330d6e5e869ff3893bcf64fd')
    with open('./fruitbowl.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            owners='IBM,me')
    print(json.dumps(classes, indent=2))
    menu_options1()


#create a custom model
def add_model():
    visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='9769d7adc1619cfc330d6e5e869ff3893bcf64fd')
    with open('./beagle.zip', 'rb') as beagle, open(
            './golden-retriever.zip', 'rb') as goldenretriever, open(
                './husky.zip', 'rb') as husky, open(
                    './cats.zip', 'rb') as cats:
        model = visual_recognition.create_classifier(
            'dogs',
            beagle_positive_examples=beagle,
            goldenretriever_positive_examples=goldenretriever,
            husky_positive_examples=husky,
            negative_examples=cats)
    print(json.dumps(model, indent=2))
    menu_options1()

#posts all current classifiers in JSON format
def see_models():
    print(get_classifiers())
    menu_options1()


#deletes selected model
def remove_model():
    visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='9769d7adc1619cfc330d6e5e869ff3893bcf64fd')
    clss = get_classifiers()
    try:
        classifier = input('Which classifier would you like removed? (list begins at 0) \n')
        response = visual_recognition.delete_classifier(classifier_id=clss['classifiers'][int(classifier)]['classifier_id'])
        print(json.dumps(response, indent=2))
        menu_options1() 
    except:
        print('No available classifiers \n')
        menu_options1()

#add new examples to classifiers
def append_model():
    clss = get_classifiers()
    visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    api_key='9769d7adc1619cfc330d6e5e869ff3893bcf64fd')
    with open('./dalmatian.zip', 'rb') as dalmatian, open(
            './more-cats.zip', 'rb') as more_cats:
        updated_model = visual_recognition.update_classifier(
            classifier_id=clss['classifiers'][0]['classifier_id'],
            dalmatian_positive_examples=dalmatian,
            negative_examples=more_cats)
    print(json.dumps(updated_model, indent=2))
    menu_options1()

#quite program
def exit():
    os.system("clear")
    sys.exit()
    
def menu_options1():
    print('Please select a menu option:')
    print('1. Classify an image')
    print('2. Create dog model')
    print('3. See posted models')
    print('4. Remove the dog model')
    print('5. Append dog model')
    print('6. Quit')
    choice = input(">>>")
    menu_options[choice]()

menu_options = {
    '1':classify_image, 
    '2':add_model, 
    '3':see_models, 
    '4':remove_model,
    '5':append_model, 
    '6':exit
    }


if __name__ == "__main__":
    print('Welcome to WATSON VISUAL ANALYZER \n')
    menu_options1()
