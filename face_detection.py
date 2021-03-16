# import PythonSDK
from PythonSDK.facepp import API,File

from PopupMsg import PopupMsg

class FaceDetection:
    def __init__(self, faceset, img_file, main_window, speaker, arduino):
        # 初始化对象，进行api的调用工作
        self.api = API()
        self.faceset = faceset
        self.img_file = img_file
        self.main = main_window
        self.speaker = speaker
        self.arduino = arduino
        self.face_ids = []
        self.face_tokens = []
        self.popupMsg = PopupMsg()
        try:
            facetokens = self.api.faceset.getdetail(outer_id=faceset)
            for facetoken in facetokens.face_tokens:
                try:
                    res = self.api.face.getdetail(face_token=facetoken)
                    self.face_ids.append(res.user_id)
                    self.face_tokens.append(facetoken)
                    print('faces: ', res)
                except:
                    self.popupMsg.popupmsg('API error', 'face.getdetail')
        except:
            try:
                ret = self.api.faceset.create(outer_id=faceset)
            except:
                self.popupMsg.popupmsg('API error', 'faceset.create')

    def identify(self):
        try:
            search_result = self.api.search(image_file=File(self.img_file), outer_id=self.faceset)
            face_confidence = search_result.results[0].confidence
            user_name = search_result.results[0].user_id
            if face_confidence > 50:
                self.main.name.setPlainText(user_name)
                self.speaker.speakMsg(user_name+'，你好，欢迎回来')
                self.arduino.open_door()
            else:
                self.speaker.speakMsg("对不起，没有你的记录")
        except:
            self.popupMsg.popupmsg('人脸检测API调用失败', '人脸检测')

    def addFace(self):
        user_name = self.main.name.toPlainText()
        print(user_name)
        if user_name:
            try:
                res = self.api.detect(image_file=File(self.img_file))
                faceList = res.faces
                if len(faceList) > 0:
                    try:
                        self.api.faceset.addface(outer_id=self.faceset, face_tokens=faceList[0].face_token)
                        try:
                            self.api.face.setuserid(face_token=faceList[0].face_token, user_id=user_name)
                            self.face_ids.append(user_name)
                            self.face_tokens.append(faceList[0].face_token)
                            self.popupMsg.popupmsg('加了: '+user_name, '增加人脸')
                        except:
                            self.popupMsg.popupmsg('设置人脸名字失败', '增加人脸')
                    except:
                        self.popupMsg.popupmsg('增加人脸失败', '增加人脸')
                else:
                    self.popupMsg.popupmsg('检测不到人脸', '增加人脸')
            except:
                self.popupMsg.popupmsg('检测人脸失败', '增加人脸')
        else:
            self.popupMsg.popupmsg('请输入名字', '增加人脸')
        self.main.name.setPlainText("")

    def deleteFace(self):
        user_name = self.main.name.toPlainText()
        name_deleted = False
        if user_name:
            i = 0
            for user_id in self.face_ids:
                if user_name == user_id:
                    try:
                        res = self.api.faceset.removeface(outer_id=self.faceset, face_tokens=self.face_token[i])
                        if res.face_removed > 0:
                            self.face_ids.remove(user_name)
                            self.face_tokens.remove(self.face_token[i])
                            self.popupMsg.popupmsg('删除了: '+user_name, '删除人脸')
                            name_deleted = True
                            break
                        else:
                            self.popupMsg.popupmsg('删除人脸失败: ' + user_name, '删除人脸')
                    except:
                        self.popupMsg.popupmsg('删除人脸失败: '+user_name, '删除人脸')
                i += 1
            if not name_deleted:
                self.popupMsg.popupmsg('找不到: '+user_name, '删除人脸')
            self.main.name.setPlainText("")
        else:
            self.popupMsg.popupmsg('请输入名字', '删除人脸')

