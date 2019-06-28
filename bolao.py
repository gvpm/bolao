from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
from pymongo import MongoClient


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

    #print("Concurso "+numeroConcurso)


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
        for document in cursor:
            #print(document)
            apostas = document["apostas"]
            concursoInicial = document["concursoInicial"]
            tamanhoCiclo = document["tamanhoCiclo"]

            url = 'https://www.lotodicas.com.br/api/mega-sena'
            resp = requests.get(url=url)
            data = resp.json()
            concursoAtual = data['numero']

            tamanhoCicloAtual = (concursoAtual - (concursoInicial-1)) % tamanhoCiclo

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

                #dezenasSorteadas=[8,18,20,24,36,45]


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

                #self.wfile.write(bytes("<p>&nbsp;</p>", "utf8"))
                # self.wfile.write(bytes("<center><font size=\"10\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                # self.wfile.write(bytes("<tr>", "utf8"))
                # self.wfile.write(bytes("<th bgcolor=\"#fff\"><font color=\"#000000\"><center></center></font></th>","utf8"))
                # self.wfile.write(bytes("</tr>", "utf8"))  
                # self.wfile.write(bytes("<tr>", "utf8"))
                # self.wfile.write(bytes("<td bgcolor=\"#fff\"><font color=\"#000000\"><center></center></font></td>","utf8"))
                # self.wfile.write(bytes("</tr>", "utf8")) 
                # self.wfile.write(bytes("<tr>", "utf8"))
                # self.wfile.write(bytes("<th bgcolor=\"#fff\"><font color=\"#000000\"><center></center></font></th>","utf8"))
                # self.wfile.write(bytes("</tr>", "utf8"))  
                # self.wfile.write(bytes("<tr>", "utf8"))
                # self.wfile.write(bytes("<td bgcolor=\"#fff\"><font color=\"#000000\"><center></center></font></td>","utf8"))
                # self.wfile.write(bytes("</tr>", "utf8")) 
                # self.wfile.write(bytes("</center></font></table>", "utf8"))

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
