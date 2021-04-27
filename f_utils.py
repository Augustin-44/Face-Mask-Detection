import torch
import os
import numpy as np
from torchvision import models, transforms
import torch.optim as optim
import time
import copy
from PIL import Image
from datetime import date
import cv2

# facemask_detection.py

def main_facemask_detection(cap):
    print("Je rentre dans la fonction")
    # ATTENTION : il est important de ne pas avoir d'espace dans le path absolu des fichiers sinon erreur avec readNet
    FRAME_THICKNESS = 2
    modelFile = os.getcwd() + os.sep + "models" + os.sep + "res10_300x300_ssd_iter_140000.caffemodel"
    configFile = os.getcwd() + os.sep + "models" + os.sep + "deploy-prototxt.txt"
    print(configFile)
    print(os.path.isfile(configFile))
    net = cv2.dnn.readNet(configFile, modelFile)

    GREEN = (0, 255, 0)
    ORANGE = (0, 165, 255)
    RED = (0, 0, 255)
    BLUE = (255, 0, 0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.6
    num_classes = 3

    image_transforms = transforms.Compose([transforms.Resize(size=(224, 224)), transforms.ToTensor(),
                                           transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    resnet18 = models.resnet18(pretrained=True)
    vgg16 = models.vgg16(pretrained=True)
    densenet = models.densenet161(pretrained=True)
    googlenet = models.googlenet(pretrained=True)
    shufflenet = models.shufflenet_v2_x1_0(pretrained=True)
    mobilenet_v3_large = models.mobilenet_v3_large(pretrained=True)
    resnext50_32x4d = models.resnext50_32x4d(pretrained=True)
    wide_resnet50_2 = models.wide_resnet50_2(pretrained=True)
    mnasnet = models.mnasnet1_0(pretrained=True)

    cnn_models = [resnet18, vgg16, densenet, googlenet, shufflenet, mobilenet_v3_large, resnext50_32x4d,
                  wide_resnet50_2, mnasnet]
    init_models(cnn_models, num_classes)

    resnet18.load_state_dict(torch.load(r"models\facemask1500\resnet18_10epochs_10bs.pth"))
    vgg16.load_state_dict(torch.load(r"models\facemask1500\vgg16_10epochs_10bs.pth"))
    densenet.load_state_dict(torch.load(r"models\facemask1500\densenet_10epochs_10bs.pth"))
    googlenet.load_state_dict(torch.load(r"models\facemask1500\googlenet_10epochs_10bs.pth"))
    mnasnet.load_state_dict(torch.load(r"models\facemask1500\mnasnet_10epochs_10bs.pth"))
    mobilenet_v3_large.load_state_dict(torch.load(r"models\facemask1500\mobilenet_v3_large_10epochs_10bs.pth"))
    resnext50_32x4d.load_state_dict(torch.load(r"models\facemask1500\resnext50_32x4d_10epochs_10bs.pth"))
    shufflenet.load_state_dict(torch.load(r"models\facemask1500\shufflenet_10epochs_10bs.pth"))
    wide_resnet50_2.load_state_dict(torch.load(r"models\facemask1500\wide_resnet50_2_10epochs_10bs.pth"))

    cnn_models = [vgg16, resnext50_32x4d, densenet]

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for model in cnn_models:
        model.eval()
        model = model.to(device)

    preds_words = ['Correct', 'Incorrect', 'NoMask']
    preds_color = [GREEN, ORANGE, RED]
    color = BLUE
    text = 'Undefined'
    fps = 0
    faces_preds_list = []
    last_faces_count = 0
    faces_change = False


    # Main Loop
    while True:
        img = cap.read()[1]
        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
        net.setInput(blob)
        faces = net.forward()
        faces_count = 0

        for j in range(faces.shape[2]):
            confidence = faces[0, 0, j, 2]
            if confidence > 0.5:
                faces_count += 1

        if faces_count != last_faces_count:
            faces_change = True
            last_faces_count = faces_count

        faces_count = 0
        if fps == 15 or faces_change:
            fps = 0
            faces_change = False
            faces_preds_list = []

        for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2]
            if confidence > 0.5:
                # print("Tete n° :", faces_count)
                faces_count += 1
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                # print(x, y, x1, y1)
                preds_list = []

                if fps == 0:
                    # DEBUT IF
                    img_face = img[y:y1, x:x1]
                    img_opencv = cv2.resize(img_face, (224, 224))
                    img_opencv = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2RGB)
                    img_pil = Image.fromarray(img_opencv)
                    img_tensor = image_transforms(img_pil).unsqueeze_(0)
                    img_tensor = img_tensor.to(device)

                    for model in cnn_models:
                        output = model(img_tensor)
                        _, preds = torch.max(output, 1)
                        preds_list.append(preds[0].item())

                    output_avg, vgg16_flag = get_output_count(preds_list)
                    index_value = get_index_max(output_avg, vgg16_flag)
                    print(preds_list, index_value)
                    text = preds_words[index_value]
                    color = preds_color[index_value]
                    faces_preds_list.append([text, color])
                    # FIN IF

                cv2.rectangle(img, (x, y), (x1, y1), faces_preds_list[faces_count-1][1], FRAME_THICKNESS)
                cv2.putText(img, faces_preds_list[faces_count-1][0], (x+10, y+20), font, fontScale, faces_preds_list[faces_count-1][1], 2, cv2.LINE_AA)

        fps += 1
        cv2.imshow('webcam', img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
             break


    cap.release()
    cv2.destroyAllWindows()


def main_facemask_detection_old(cap):

    # DOES NOT WORK ON MULTIPLES FACES
    # ATTENTION : il est important de ne pas avoir d'espace dans le path absolu des fichiers sinon erreur avec readNet

    FRAME_THICKNESS = 2
    modelFile = os.getcwd() + os.sep + "models" + os.sep + "res10_300x300_ssd_iter_140000.caffemodel"
    configFile = os.getcwd() + os.sep + "models" + os.sep + "deploy-prototxt.txt"
    print(configFile)
    print(os.path.isfile(configFile))
    net = cv2.dnn.readNet(configFile, modelFile)

    GREEN = (0, 255, 0)
    ORANGE = (0, 165, 255)
    RED = (0, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (25, 50)
    fontScale = 1
    num_classes = 3

    image_transforms = transforms.Compose([transforms.Resize(size=(224, 224)), transforms.ToTensor(),
                                           transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    resnet18 = models.resnet18(pretrained=True)
    vgg16 = models.vgg16(pretrained=True)
    densenet = models.densenet161(pretrained=True)
    googlenet = models.googlenet(pretrained=True)
    shufflenet = models.shufflenet_v2_x1_0(pretrained=True)
    mobilenet_v3_large = models.mobilenet_v3_large(pretrained=True)
    resnext50_32x4d = models.resnext50_32x4d(pretrained=True)
    wide_resnet50_2 = models.wide_resnet50_2(pretrained=True)
    mnasnet = models.mnasnet1_0(pretrained=True)

    cnn_models = [resnet18, vgg16, densenet, googlenet, shufflenet, mobilenet_v3_large, resnext50_32x4d,
                  wide_resnet50_2, mnasnet]
    init_models(cnn_models, num_classes)

    resnet18.load_state_dict(torch.load(r"models\facemask1500\resnet18_10epochs_10bs.pth"))
    vgg16.load_state_dict(torch.load(r"models\facemask1500\vgg16_10epochs_10bs.pth"))
    densenet.load_state_dict(torch.load(r"models\facemask1500\densenet_10epochs_10bs.pth"))
    googlenet.load_state_dict(torch.load(r"models\facemask1500\googlenet_10epochs_10bs.pth"))
    mnasnet.load_state_dict(torch.load(r"models\facemask1500\mnasnet_10epochs_10bs.pth"))
    mobilenet_v3_large.load_state_dict(torch.load(r"models\facemask1500\mobilenet_v3_large_10epochs_10bs.pth"))
    resnext50_32x4d.load_state_dict(torch.load(r"models\facemask1500\resnext50_32x4d_10epochs_10bs.pth"))
    shufflenet.load_state_dict(torch.load(r"models\facemask1500\shufflenet_10epochs_10bs.pth"))
    wide_resnet50_2.load_state_dict(torch.load(r"models\facemask1500\wide_resnet50_2_10epochs_10bs.pth"))

    cnn_models = [vgg16, resnext50_32x4d, densenet]

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for model in cnn_models:
        model.eval()
        model = model.to(device)

    preds_words = ['Correct', 'Incorrect', 'NoMask']
    preds_color = [GREEN, ORANGE, RED]
    color = RED
    text = 'NoMask'
    fps = 0
    img_list = []

    # Main Loop
    while True:
        img = cap.read()[1]
        if fps == 60 :
            fps = 0

        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
        net.setInput(blob)
        faces = net.forward()

        for i in range(faces.shape[2]):

            confidence = faces[0, 0, i, 2]
            if confidence > 0.5:
                box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                print(x, y, x1, y1)
                preds_list = []

                # number= time.time()
                # frame = int((str(number-int(number))[1:])[1:3])
                if fps % 30 == 0:
                    img_face = img[y:y1, x:x1]
                    img_opencv = cv2.resize(img_face, (224, 224))
                    img_opencv = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2RGB)
                    img_pil = Image.fromarray(img_opencv)
                    img_tensor = image_transforms(img_pil).unsqueeze_(0)
                    img_tensor = img_tensor.to(device)

                    for model in cnn_models:
                        output = model(img_tensor)
                        _, preds = torch.max(output, 1)
                        preds_list.append(preds[0].item())

                    output_avg, vgg16_flag = get_output_count(preds_list)
                    index_value = get_index_max(output_avg, vgg16_flag)
                    print(preds_list, index_value)
                    text = preds_words[index_value]
                    color = preds_color[index_value]

                #text = preds_words[random.randint(0, 2)]
                cv2.rectangle(img, (x, y), (x1, y1), color, FRAME_THICKNESS)
                cv2.putText(img, text, (x-10, y+10), font, fontScale, color, 2, cv2.LINE_AA)

        fps += 1
        cv2.imshow('webcam', img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

    return

def list_ports():
    is_working = True
    index = 0
    while is_working:
        camera = cv2.VideoCapture(index)
        if not camera.isOpened():
            is_working = False
        else:
            is_reading, img = camera.read()
            if is_reading:
                index += 1

    return index





def add_img_to_list(img, img_list):
    tmp = img_list
    if len(img_list) == 0:
        img
    return img_list



def get_output_count(preds_list):
    values_list = [0, 1, 2]
    values_count = [0, 0, 0]
    vgg16_flag = False

    for element in preds_list:
        if element == values_list[0]:
            values_count[0] += 1
        elif element == values_list[1]:
            values_count[1] += 1
        elif element == values_list[2]:
            values_count[2] += 1
    if preds_list[0] == 1:
        vgg16_flag = True
    return values_count, vgg16_flag

def get_index_max(values_count, vgg16_flag):
    index_max = None
    if vgg16_flag: # since false positives with incorrect class are low with vgg16, the cnn predict is prioritized
        index_max = 1
    else:
        for index in range(len(values_count)):
            if values_count[index] == max(values_count):
                index_max = index
    return index_max


def get_top_n_models(models_acc_list, cnn_models, n):
    tmp = models_acc_list
    l = np.array(tmp)
    top_n_idx = ((-l).argsort()[:n]).tolist()

    top_n_models = []
    for idx in top_n_idx:
        top_n_models.append(cnn_models[idx])
    return top_n_models

def set_parameter_requires_grad(model, feature_extracting): #fonction à appeler avant de modifier le dernier layer du cnn
    if feature_extracting == True:
        for param in model.parameters():
            param.requires_grad = False

def init_models(cnn_models, num_classes, feature_extracting=True):
    for index in range(len(cnn_models)):
        #print(index)
        try:
            cnn_models[index].classifier #throws error
            set_parameter_requires_grad(cnn_models[index], feature_extracting)
            errorFlag = False
            classifierCount = 0
            while(errorFlag == False):
                try:
                    cnn_models[index].classifier[classifierCount]
                    classifierCount += 1
                except IndexError or TypeError:
                    errorFlag = True

            classifierCount -= 1
            cnn_models[index].classifier[classifierCount] = torch.nn.Linear(cnn_models[index].classifier[classifierCount].in_features, out_features=num_classes, bias=True)
            #print(cnn_models[index].classifier[classifierCount])


        except AttributeError:
            #print(cnn_models[index].fc)
            set_parameter_requires_grad(cnn_models[index], feature_extracting)
            cnn_models[index].fc = torch.nn.Linear(cnn_models[index].fc.in_features, out_features=num_classes, bias=True)
            #print(cnn_models[index].fc)

        except TypeError:
            set_parameter_requires_grad(cnn_models[index], feature_extracting)
            cnn_models[index].classifier = torch.nn.Linear(cnn_models[index].classifier.in_features, out_features=num_classes, bias=True)
            #print(cnn_models[index].classifier)

    return cnn_models

def train_models(cnn_models, cnn_models_dict, train_dataset, val_dataset, feature_extracting = True, num_epochs=10, batch_size=10):

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    best_acc = 0.0
    models_path = r"models\facemask1500"
    top_models_path = r"models\facemask1500\top"
    best_model_path = r"models\facemask1500\best"
    logs_path = r"models\facemask1500\logs"
    models_acc_list = []
    best_model = None
    prev_best_path = None


    d1 = date.today().strftime("%d-%m-%Y")
    f = open(logs_path + os.sep + "train_models_" + str(d1) +"_" + str(num_epochs) + "epochs" + "_" + str(batch_size) + "bs" + ".txt", "w")
    f.write("Training done on: {} \nFeature extracting:{}\n".format(d1, feature_extracting))

    for model in cnn_models:
        print(cnn_models_dict[model])
        f.write("\n{}\n".format(cnn_models_dict[model]))

        best_acc_model = 0.0
        val_acc_history = []
        best_model_wts = copy.deepcopy(model.state_dict())
        since = time.time()

        # si num_workers != 0 : ERREUR
        val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=0)
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=0)
        dataloaders = {'train': train_loader, 'val': val_loader}
        criterion = torch.nn.CrossEntropyLoss()

        model = model.to(device)
        params_to_update = model.parameters()
        print("Params to learn:")
        if feature_extracting:
            params_to_update = []
            for name, param in model.named_parameters():
                if param.requires_grad == True:
                    params_to_update.append(param)
                    print("\t", name)
        else:
            for name, param in model.named_parameters():
                if param.requires_grad == True:
                    print("\t", name)

        optimizer = optim.SGD(params_to_update, lr=0.001, momentum=0.9)

        for epoch in range(num_epochs):
            print('\nEpoch {}/{}'.format(epoch, num_epochs - 1))
            print('-' * 10)
            f.write('\nEpoch {}/{}\n'.format(epoch, num_epochs - 1))
            f.write("-----------\n")

            # Each epoch has a training and validation phase
            for phase in ['train', 'val']:
                if phase == 'train':
                    model.train()  # Set model to training mode
                else:
                    model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    # track history if only in train
                    with torch.set_grad_enabled(phase == 'train'):
                        # Get model outputs and calculate loss
                        # In train mode we calculate the loss by summing the final output and the auxiliary output
                        #   but in testing we only consider the final output.
                        outputs = model(inputs)
                        loss = criterion(outputs, labels)

                        _, preds = torch.max(outputs, 1)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()

                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)

                epoch_loss = running_loss / len(dataloaders[phase].dataset)
                epoch_acc = running_corrects.double() / len(dataloaders[phase].dataset)

                print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))
                f.write('{} Loss: {:.4f} Acc: {:.4f}\n'.format(phase, epoch_loss, epoch_acc))

                # deep copy the model
                if phase == 'val' and epoch_acc > best_acc_model:
                    best_acc_model = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())
                    torch.save(model.state_dict(), os.path.join(models_path, cnn_models_dict[model] + "_" + str(num_epochs) + "epochs_" + str(batch_size) +"bs" + ".pth"))

                if phase == 'val':
                    val_acc_history.append(epoch_acc.item())

        models_acc_list.append(best_acc_model)

        # A la fin des epochs, on regarde si le modele est plus precis par rapport aux autres
        if best_acc_model > best_acc:
            best_acc = best_acc_model
            best_model = model
            best_model.load_state_dict(best_model_wts)
            if prev_best_path != None:
                os.remove(prev_best_path)
            torch.save(model.state_dict(), os.path.join(best_model_path, cnn_models_dict[model] + "_" + str(num_epochs) + "epochs_" + str(batch_size) +"bs" + ".pth"))
            prev_best_path = os.path.join(best_model_path, cnn_models_dict[model] + "_" + str(num_epochs) + "epochs_" + str(batch_size) +"bs" + ".pth")
            print("\n BEST MODEL SAVED\n", prev_best_path, "\n")

        time_elapsed = time.time() - since
        print('\nTraining complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
        print('Best val Acc: {:4f}'.format(best_acc))

        f.write('\nTraining complete in {:.0f}m {:.0f}s\n'.format(time_elapsed // 60, time_elapsed % 60))
        f.write('Best val Acc: {:4f}\n'.format(best_acc))
        f.write('{}\n\n\n'.format(val_acc_history))

    f.write("The 5 most accurate models are:\n")
    top_5_models = get_top_n_models(models_acc_list, cnn_models, 5)
    for model in top_5_models:
        torch.save(model.state_dict(), os.path.join(top_models_path, cnn_models_dict[model] + "_" + str(num_epochs) + "epochs_" + str(batch_size) + "bs" + ".pth"))
        f.write("{}\n".format(model.__class__.__name__))

    f.write("\n")
    f.close()

    return best_model, top_5_models
