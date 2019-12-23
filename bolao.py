from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
from pymongo import MongoClient
from urllib.parse import urlsplit, parse_qs


def getMegaSenaResult():

    url = 'https://www.lotodicas.com.br/api/mega-sena'

    params = dict(
        loteria='megasena',
        token='6YrWtz8nbAOB7FN',
    )
    resp = requests.get(url=url)
    data = resp.json()
    #resultado = json.load(data)

    numeroConcurso = data['numero']
    dataConcurso = data['data']
    dezenasSorteadas = data['sorteio']


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        client = MongoClient('gvpm.com.br')

        mongoDatabase = client.bolao

        apostasAlbum = mongoDatabase.apostas

        #print(str(apostasAlbum))

        apostas = []
        cursor = apostasAlbum.find({})
        for 1 in (1):
            #print(document)
            apostas = [[3, 9, 14, 29, 32, 57],[15, 19, 37, 41, 42, 47],[7, 14, 32, 34, 58, 60],[22, 25, 35, 44, 46, 48],[3, 12, 35, 51, 57, 58],[5, 10, 23, 33, 42, 54],[8, 9, 15, 24, 33, 60],[2, 11, 35, 37, 40, 56],[6, 10, 11, 38, 49, 52],[9, 19, 28, 29, 52, 54],[5, 10, 12, 18, 25, 32],[1, 10, 15, 16, 22, 33],[3, 7, 20, 26, 42, 44],[9, 16, 23, 31, 57, 60],[2, 18, 19, 33, 35, 53],[1, 7, 18, 20, 21, 57],[3, 8, 32, 33, 51, 58],[8, 18, 25, 35, 43, 53],[1, 10, 18, 28, 44, 60],[6, 14, 27, 35, 40, 53],[1, 13, 34, 39, 45, 54],[21, 30, 35, 37, 46, 51],[3, 7, 15, 29, 51, 52],[5, 7, 9, 12, 19, 50],[4, 10, 28, 34, 46, 54],[6, 15, 18, 20, 21, 35],[4, 6, 35, 43, 47, 50],[5, 14, 22, 38, 55, 57],[11, 18, 28, 29, 31, 32],[17, 21, 25, 30, 31, 41],[16, 27, 36, 39, 40, 50],[5, 7, 16, 36, 45, 52],[3, 4, 16, 23, 31, 52],[1, 18, 24, 27, 47, 56],[1, 15, 22, 27, 31, 49],[6, 14, 26, 35, 43, 55],[5, 15, 38, 40, 42, 59],[5, 22, 26, 35, 36, 52],[15, 24, 30, 34, 37, 58],[19, 21, 22, 30, 39, 43],[23, 31, 34, 37, 38, 60],[24, 27, 48, 50, 55, 59],[14, 17, 21, 23, 57, 60],[5, 12, 23, 31, 36, 46],[12, 29, 32, 33, 46, 50],[2, 34, 39, 47, 48, 51],[5, 6, 18, 28, 35, 54],[21, 28, 29, 39, 55, 57],[3, 16, 22, 28, 32, 39],[5, 12, 18, 23, 29, 59],[20, 32, 47, 53, 58, 60],[9, 10, 33, 40, 43, 45],[4, 8, 42, 44, 45, 51],[15, 17, 19, 24, 46, 49],[6, 11, 18, 45, 50, 51],[4, 5, 13, 17, 34, 55],[12, 13, 15, 24, 39, 40],[20, 24, 28, 39, 41, 53],[3, 10, 28, 31, 47, 49],[2, 3, 6, 50, 56, 60],[11, 22, 43, 49, 56, 58],[6, 28, 30, 31, 35, 55],[1, 7, 18, 46, 52, 55],[27, 36, 42, 44, 45, 51],[5, 38, 40, 44, 57, 59],[13, 16, 20, 38, 57, 58],[1, 17, 19, 41, 49, 50],[4, 22, 28, 31, 32, 47],[1, 17, 18, 23, 52, 56],[18, 21, 24, 32, 43, 47],[1, 12, 14, 21, 22, 45],[8, 14, 16, 35, 47, 53],[8, 11, 12, 15, 43, 45],[9, 12, 13, 15, 28, 35],[7, 34, 37, 46, 50, 56],[1, 2, 3, 16, 17, 56],[3, 23, 29, 36, 40, 52],[28, 45, 46, 47, 49, 53],[10, 13, 38, 40, 42, 47],[1, 16, 22, 26, 29, 30],[18, 22, 39, 44, 51, 58],[6, 7, 26, 34, 44, 54],[8, 13, 20, 42, 50, 51],[10, 17, 35, 46, 54, 57],[2, 7, 9, 12, 41, 50],[9, 23, 39, 44, 45, 57],[2, 13, 25, 32, 39, 46],[3, 14, 26, 29, 31, 54],[3, 4, 22, 24, 50, 57],[1, 13, 29, 39, 43, 59],[3, 15, 20, 31, 32, 43],[22, 29, 40, 57, 58, 60],[2, 31, 34, 38, 49, 60],[6, 42, 43, 50, 54, 58],[13, 15, 18, 27, 45, 58],[11, 17, 23, 24, 33, 48],[11, 33, 37, 39, 45, 58],[15, 17, 30, 31, 50, 51],[14, 23, 33, 35, 41, 44],[8, 12, 14, 17, 18, 26],[9, 14, 26, 27, 33, 40],[7, 23, 28, 38, 47, 53],[4, 5, 7, 8, 24, 44],[5, 15, 30, 40, 55, 56],[9, 23, 25, 43, 54, 59],[3, 9, 13, 17, 26, 40],[4, 8, 13, 38, 40, 45],[1, 11, 37, 39, 47, 50],[3, 15, 28, 41, 55, 57],[4, 11, 34, 36, 37, 54],[19, 29, 30, 51, 55, 58],[14, 17, 28, 29, 41, 46],[7, 17, 25, 38, 47, 58],[20, 24, 25, 35, 36, 55],[8, 18, 24, 27, 34, 42],[1, 6, 35, 36, 42, 51],[3, 6, 13, 15, 21, 55],[7, 14, 19, 37, 38, 45],[2, 10, 16, 19, 59, 60],[3, 9, 25, 31, 41, 45],[7, 18, 25, 44, 54, 55],[1, 4, 37, 43, 55, 60],[8, 18, 29, 31, 35, 40],[1, 7, 30, 35, 43, 48],[16, 17, 19, 44, 53, 55],[8, 23, 24, 46, 47, 52],[2, 10, 35, 55, 56, 59],[2, 15, 19, 37, 54, 55],[3, 26, 34, 41, 56, 58],[3, 5, 13, 27, 36, 52],[4, 13, 14, 16, 30, 44],[17, 38, 44, 46, 49, 54],[1, 6, 16, 33, 43, 56]]
            concursoInicial = 2220
            tamanhoCiclo = 1


            dezenasConsulta=[]
            query = urlsplit(self.path).query
            params = dict(parse_qs(query))
            if params:
                dezenasConsulta = params["jogo"] 
                #print(dezenasConsulta[0])                    
                #dezenasSorteadas="["+dezenasConsulta[0]+"]"
                dezenasSorteadas=(dezenasConsulta[0].split(','))
                #print(dezenasSorteadas)
                dezenasSorteadas = [int(i) for i in dezenasSorteadas]
                #print(dezenasSorteadas)

                url = ("https://www.lotodicas.com.br/api/mega-sena/")

                resp = requests.get(url=url)
                data = resp.json()

                numeroConcurso = data['numero']
                dataConcurso = data['data']
                #dezenasSorteadas = data['sorteio']
                proximaData = data['proximo_data']
                acumulado = data['acumulado']
                proximaEstimativa = data['proximo_estimativa']
                ganhadores = data['ganhadores']
                rateio = data['rateio']

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                apostasCom6 = []
                apostasCom5 = []
                apostasCom4 = []
                apostasCom3 = []
                apostasCom2 = []
                apostasCom1 = []
                apostasCom0 = []
                for aposta in apostas:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    if numberOfMatched == 6:
                        apostasCom6.append(aposta)
                    elif numberOfMatched == 5:
                        apostasCom5.append(aposta)
                    elif numberOfMatched == 4:
                        apostasCom4.append(aposta)
                    elif numberOfMatched == 3:
                        apostasCom3.append(aposta)
                    elif numberOfMatched == 2:
                        apostasCom2.append(aposta)
                    elif numberOfMatched == 1:
                        apostasCom1.append(aposta)
                    elif numberOfMatched == 0:
                        apostasCom0.append(aposta)
                self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                self.wfile.write(bytes("<tr>", "utf8"))
                self.wfile.write(bytes("<th bgcolor=\"#FF0000\"><font color=\"#000000\"><center>Dezenas Consultadas</center></font></th>","utf8"))
                self.wfile.write(bytes("</tr>", "utf8"))  
                self.wfile.write(bytes("<tr>", "utf8"))
                self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(dezenasSorteadas)+"</center></font></td>","utf8"))
                self.wfile.write(bytes("</tr>", "utf8")) 
                self.wfile.write(bytes("</center></font></table>", "utf8"))
                self.wfile.write(bytes("<center><table style=\"width:100%\">", "utf8"))
                self.wfile.write(bytes("<tr>", "utf8"))
                self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>Jogo</center></font></th>","utf8"))
                self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>QtdAcertos</center></font></th>","utf8"))
                self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>Acertos</center></font></th>","utf8"))
                self.wfile.write(bytes("</tr>", "utf8"))  
                if len(apostasCom6) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 6 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom6:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))                 
                if len(apostasCom5) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 5 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom5:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                if len(apostasCom4) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 4 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom4:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                if len(apostasCom3) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 3 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom3:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                if len(apostasCom2) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 2 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom2:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                if len(apostasCom1) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 1 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom1:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                if len(apostasCom0) > 0:
                    #self.wfile.write(bytes("<center><h3>Apostas com 0 acertos</h3></center>", "utf8"))
                    for aposta in apostasCom0:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center> </center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))      
                
            else:
                url = 'https://www.lotodicas.com.br/api/mega-sena'
                resp = requests.get(url=url)
                data = resp.json()
                concursoAtual = data['numero']


                tamanhoCicloAtual = (concursoAtual - (concursoInicial-1)) % tamanhoCiclo
                print(str(tamanhoCicloAtual))
                if tamanhoCicloAtual == 0:
                    tamanhoCicloAtual = tamanhoCiclo

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                ultimoDoCicloAnterior=concursoAtual-tamanhoCicloAtual

                sorteiosNoCiclo=""
                for x in range(1, 9):
                #     concurso = concursoAtual-x
                    sorteiosNoCiclo = sorteiosNoCiclo+" "+ str(ultimoDoCicloAnterior + x)

                print(sorteiosNoCiclo)

                self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                self.wfile.write(bytes("<tr>", "utf8"))
                self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Sorteios No Ciclo</center></font></th>","utf8"))
                self.wfile.write(bytes("</tr>", "utf8"))  
                self.wfile.write(bytes("<tr>", "utf8"))
                self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + sorteiosNoCiclo +"</center></font></td>","utf8"))
                self.wfile.write(bytes("</tr>", "utf8")) 
                self.wfile.write(bytes("</center></font></table>", "utf8"))





                for x in range(0, tamanhoCicloAtual):
                    concurso = concursoAtual-x

                    url = ("https://www.lotodicas.com.br/api/mega-sena/"+ str(concurso))

                    resp = requests.get(url=url)
                    data = resp.json()

                    numeroConcurso = data['numero']
                    dataConcurso = data['data']
                    dezenasSorteadas = data['sorteio']
                    proximaData = data['proximo_data']
                    acumulado = data['acumulado']
                    proximaEstimativa = data['proximo_estimativa']
                    ganhadores = data['ganhadores']
                    rateio = data['rateio']






                    my_json_string = json.dumps(apostas)
                    #print(my_json_string)

                    apostasCom6 = []
                    apostasCom5 = []
                    apostasCom4 = []
                    apostasCom3 = []
                    apostasCom2 = []
                    apostasCom1 = []
                    apostasCom0 = []
                    for aposta in apostas:
                        matches = set(dezenasSorteadas) & set(aposta)
                        numberOfMatched = len(matches)
                        if numberOfMatched == 6:
                            apostasCom6.append(aposta)
                        elif numberOfMatched == 5:
                            apostasCom5.append(aposta)
                        elif numberOfMatched == 4:
                            apostasCom4.append(aposta)
                        elif numberOfMatched == 3:
                            apostasCom3.append(aposta)
                        elif numberOfMatched == 2:
                            apostasCom2.append(aposta)
                        elif numberOfMatched == 1:
                            apostasCom1.append(aposta)
                        elif numberOfMatched == 0:
                            apostasCom0.append(aposta)




                    self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#FF0000\"><font color=\"#000000\"><center>Concurso</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(numeroConcurso)+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#FF0000\"><font color=\"#000000\"><center>Acumulado</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(acumulado).upper()+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#FF0000\"><font color=\"#000000\"><center>Data</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(dataConcurso)+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#FF0000\"><font color=\"#000000\"><center>Dezenas Sorteadas</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(dezenasSorteadas)+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("</center></font></table>", "utf8"))


                    self.wfile.write(bytes("<center><table style=\"width:100%\">", "utf8"))

                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>Jogo</center></font></th>","utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>QtdAcertos</center></font></th>","utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#4169E1\"><font color=\"#000000\"><center>Acertos</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  

                    if len(apostasCom6) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 6 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom6:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))                 

                    if len(apostasCom5) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 5 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom5:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    if len(apostasCom4) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 4 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom4:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    if len(apostasCom3) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 3 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom3:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    if len(apostasCom2) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 2 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom2:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    if len(apostasCom1) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 1 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom1:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    if len(apostasCom0) > 0:
                        #self.wfile.write(bytes("<center><h3>Apostas com 0 acertos</h3></center>", "utf8"))
                        for aposta in apostasCom0:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)

                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center> </center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                    self.wfile.write(bytes("</center></table>", "utf8"))



                    self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos na Sena</center></font></th>","utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores[0])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio[0])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos na Quina</center></font></th>","utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores[1])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio[1])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos na Quadra</center></font></th>","utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores[2])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio[2])+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))
                    self.wfile.write(bytes("</center></font></table>", "utf8"))
                    self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Proximo Concurso</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(proximaData)+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Valor Estimado</center></font></th>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8"))  
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>R$" + str(proximaEstimativa)+"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("</center></font></table>", "utf8"))


        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 666)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
