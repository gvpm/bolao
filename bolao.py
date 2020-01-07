from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
from pymongo import MongoClient
from urllib.parse import urlsplit, parse_qs



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

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        for document in cursor:
            #print(document)
            apostas = document["apostas"]
            #print(apostas)
            concursoInicial = document["concursoInicial"]
            tamanhoCiclo = document["tamanhoCiclo"]
            tipo = document["tipo"]
            
            if tipo == "mega":
                dezenasConsulta=[]
                query = urlsplit(self.path).query
                params = dict(parse_qs(query))
                if params:
                    dezenasConsulta = params["jogo"] 

                    dezenasSorteadas=(dezenasConsulta[0].split(','))

                    dezenasSorteadas = [int(i) for i in dezenasSorteadas]

                    url = ("http://apiloterias.com.br/api0/json.php?loteria=megasena&concurso=")


                    resp = requests.get(url=url)
                    data = resp.json()


                    numeroConcurso = data['concurso']['numero']
                    dataConcurso = data['concurso']['data']
                    proximaData = data['proximo_concurso']['data']
                    acumulado = data['concurso']['valor_acumulado']
                    proximaEstimativa = data['proximo_concurso']['valor_estimado']

                    ganhadoresSena = data['concurso']['premiacao']['sena']['ganhadores']
                    rateioSena = data['concurso']['premiacao']['sena']['valor_pago']
                    ganhadoresQuina = data['concurso']['premiacao']['quina']['ganhadores']
                    rateioQuina = data['concurso']['premiacao']['quina']['valor_pago']
                    ganhadoresQuadra = data['concurso']['premiacao']['quadra']['ganhadores']
                    rateioQuadra = data['concurso']['premiacao']['quadra']['valor_pago'] 

                    # self.send_response(200)
                    # self.send_header('Content-type', 'text/html')
                    # self.end_headers()
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
                        for aposta in apostasCom6:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))                 
                    if len(apostasCom5) > 0:
                        for aposta in apostasCom5:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom4) > 0:
                        for aposta in apostasCom4:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom3) > 0:
                        for aposta in apostasCom3:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom2) > 0:
                        for aposta in apostasCom2:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom1) > 0:
                        for aposta in apostasCom1:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom0) > 0:
                        for aposta in apostasCom0:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center> </center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                else:

                    url= 'http://apiloterias.com.br/api0/json.php?loteria=megasena&concurso='
                    resp = requests.get(url=url)
                    data = resp.json()
                    #print(data)
                    concursoAtual = int(data['concurso']['numero'])


                    tamanhoCicloAtual = (concursoAtual - (concursoInicial-1)) % tamanhoCiclo
                    #print(str(tamanhoCicloAtual))
                    if tamanhoCicloAtual == 0:
                        tamanhoCicloAtual = tamanhoCiclo

                    # self.send_response(200)
                    # self.send_header('Content-type', 'text/html')
                    # self.end_headers()

                    ultimoDoCicloAnterior=concursoAtual-tamanhoCicloAtual

                    sorteiosNoCiclo=""
                    for x in range(1, 9):
                        sorteiosNoCiclo = sorteiosNoCiclo+" "+ str(ultimoDoCicloAnterior + x)

                    #print(sorteiosNoCiclo)

                    self.wfile.write(bytes("<center><font size=\"100\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#993399\"><font color=\"#000000\"><center>" + tipo.upper() +"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("</center></font></table>", "utf8"))


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


                        url = ("http://apiloterias.com.br/api0/json.php?loteria=megasena&concurso="+ str(concurso))


                        resp = requests.get(url=url)
                        data = resp.json()

                        numeroConcurso = data['concurso']['numero']
                        dataConcurso = data['concurso']['data']
                        dezenasSorteadas = data['concurso']['dezenas']
                        dezenasSorteadas = list(map(int, dezenasSorteadas))

                        proximaData = data['proximo_concurso']['data']
                        acumulado = data['concurso']['valor_acumulado']
                        proximaEstimativa = data['proximo_concurso']['valor_estimado']

                        ganhadoresSena = data['concurso']['premiacao']['sena']['ganhadores']
                        rateioSena = data['concurso']['premiacao']['sena']['valor_pago']

                        ganhadoresQuina = data['concurso']['premiacao']['quina']['ganhadores']
                        rateioQuina = data['concurso']['premiacao']['quina']['valor_pago']

                        ganhadoresQuadra = data['concurso']['premiacao']['quadra']['ganhadores']
                        rateioQuadra = data['concurso']['premiacao']['quadra']['valor_pago']                    



                        my_json_string = json.dumps(apostas)

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
                            for aposta in apostasCom6:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))                 

                        if len(apostasCom5) > 0:
                            for aposta in apostasCom5:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom4) > 0:
                            for aposta in apostasCom4:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom3) > 0:
                            for aposta in apostasCom3:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom2) > 0:
                            for aposta in apostasCom2:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom1) > 0:
                            for aposta in apostasCom1:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom0) > 0:
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
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadoresSena)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateioSena)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos na Quina</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadoresQuina)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateioQuina)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos na Quadra</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadoresQuadra)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateioQuadra)+"</center></font></td>","utf8"))
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
            elif tipo == "lotofacil":
                dezenasConsulta=[]
                query = urlsplit(self.path).query
                params = dict(parse_qs(query))
                if params:
                    dezenasConsulta = params["jogo"] 

                    dezenasSorteadas=(dezenasConsulta[0].split(','))

                    dezenasSorteadas = [int(i) for i in dezenasSorteadas]

                    url = ("http://apiloterias.com.br/api0/json.php?loteria=megasena&concurso=")


                    resp = requests.get(url=url)
                    data = resp.json()


                    numeroConcurso = data['concurso']['numero']
                    dataConcurso = data['concurso']['data']
                    proximaData = data['proximo_concurso']['data']
                    acumulado = data['concurso']['valor_acumulado']
                    proximaEstimativa = data['proximo_concurso']['valor_estimado']

                    ganhadoresSena = data['concurso']['premiacao']['sena']['ganhadores']
                    rateioSena = data['concurso']['premiacao']['sena']['valor_pago']
                    ganhadoresQuina = data['concurso']['premiacao']['quina']['ganhadores']
                    rateioQuina = data['concurso']['premiacao']['quina']['valor_pago']
                    ganhadoresQuadra = data['concurso']['premiacao']['quadra']['ganhadores']
                    rateioQuadra = data['concurso']['premiacao']['quadra']['valor_pago'] 

                    # self.send_response(200)
                    # self.send_header('Content-type', 'text/html')
                    # self.end_headers()
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
                        for aposta in apostasCom6:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#FFD300\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))                 
                    if len(apostasCom5) > 0:
                        for aposta in apostasCom5:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom4) > 0:
                        for aposta in apostasCom4:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom3) > 0:
                        for aposta in apostasCom3:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#808088\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom2) > 0:
                        for aposta in apostasCom2:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#98989C\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom1) > 0:
                        for aposta in apostasCom1:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#A9A9B0\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      
                    if len(apostasCom0) > 0:
                        for aposta in apostasCom0:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            self.wfile.write(bytes("<tr>", "utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                            self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center> </center></font></td>","utf8"))
                            self.wfile.write(bytes("</tr>", "utf8"))      

                else:

                    url= 'http://apiloterias.com.br/api0/json.php?loteria=lotofacil&concurso='
                    resp = requests.get(url=url)
                    data = resp.json()
                    #print(data)
                    concursoAtual = int(data['concurso']['numero'])


                    tamanhoCicloAtual = (concursoAtual - (concursoInicial-1)) % tamanhoCiclo
                    #print(str(tamanhoCicloAtual))
                    if tamanhoCicloAtual == 0:
                        tamanhoCicloAtual = tamanhoCiclo

                    # self.send_response(200)
                    # self.send_header('Content-type', 'text/html')
                    # self.end_headers()

                    ultimoDoCicloAnterior=concursoAtual-tamanhoCicloAtual

                    sorteiosNoCiclo=""
                    for x in range(1, 9):
                        sorteiosNoCiclo = sorteiosNoCiclo+" "+ str(ultimoDoCicloAnterior + x)

                    #print(sorteiosNoCiclo)

                    self.wfile.write(bytes("<center><font size=\"100\" face=\"Courier New\" ><table style=\"width:100%\">", "utf8"))     
                    self.wfile.write(bytes("<tr>", "utf8"))
                    self.wfile.write(bytes("<td bgcolor=\"#993399\"><font color=\"#000000\"><center>" + tipo.upper() +"</center></font></td>","utf8"))
                    self.wfile.write(bytes("</tr>", "utf8")) 
                    self.wfile.write(bytes("</center></font></table>", "utf8"))

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


                        url = ("http://apiloterias.com.br/api0/json.php?loteria=lotofacil&concurso="+ str(concurso))


                        resp = requests.get(url=url)
                        data = resp.json()

                        numeroConcurso = data['concurso']['numero']
                        dataConcurso = data['concurso']['data']
                        dezenasSorteadas = data['concurso']['dezenas']
                        dezenasSorteadas = list(map(int, dezenasSorteadas))

                        proximaData = data['proximo_concurso']['data']
                        acumulado = data['concurso']['valor_acumulado']
                        proximaEstimativa = data['proximo_concurso']['valor_estimado']

                        ganhadores15 = data['concurso']['premiacao']['acertos_15']['ganhadores']
                        rateio15 = data['concurso']['premiacao']['acertos_15']['valor_pago']
                        ganhadores14 = data['concurso']['premiacao']['acertos_14']['ganhadores']
                        rateio14 = data['concurso']['premiacao']['acertos_14']['valor_pago']
                        ganhadores13 = data['concurso']['premiacao']['acertos_13']['ganhadores']
                        rateio13 = data['concurso']['premiacao']['acertos_13']['valor_pago']
                        ganhadores12 = data['concurso']['premiacao']['acertos_12']['ganhadores']
                        rateio12 = data['concurso']['premiacao']['acertos_12']['valor_pago']                
                        ganhadores11 = data['concurso']['premiacao']['acertos_11']['ganhadores']
                        rateio11 = data['concurso']['premiacao']['acertos_11']['valor_pago']


                        my_json_string = json.dumps(apostas)


                        apostasCom15 = []
                        apostasCom14 = []
                        apostasCom13 = []
                        apostasCom12 = []
                        apostasCom11 = []
                        apostasComMenos11 = []
                        for aposta in apostas:
                            matches = set(dezenasSorteadas) & set(aposta)
                            numberOfMatched = len(matches)
                            if numberOfMatched == 15:
                                apostasCom15.append(aposta)
                            elif numberOfMatched == 14:
                                apostasCom14.append(aposta)
                            elif numberOfMatched == 13:
                                apostasCom13.append(aposta)
                            elif numberOfMatched == 12:
                                apostasCom12.append(aposta)
                            elif numberOfMatched == 11:
                                apostasCom11.append(aposta)
                            elif numberOfMatched < 11:
                                apostasComMenos11.append(aposta)




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

              

                        if len(apostasCom15) > 0:
                            for aposta in apostasCom15:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom14) > 0:
                            for aposta in apostasCom14:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom13) > 0:
                            for aposta in apostasCom13:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom12) > 0:
                            for aposta in apostasCom12:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasCom11) > 0:
                            for aposta in apostasCom11:
                                matches = set(dezenasSorteadas) & set(aposta)
                                numberOfMatched = len(matches)

                                self.wfile.write(bytes("<tr>", "utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(aposta)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(numberOfMatched)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("<td bgcolor=\"#2CD32\"><font color=\"#000000\"><center>"+str(matches)+"</center></font></td>","utf8"))
                                self.wfile.write(bytes("</tr>", "utf8"))      

                        if len(apostasComMenos11) > 0:
                            for aposta in apostasComMenos11:
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
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos com 15</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores15)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio15)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos com 14</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores14)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio14)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos com 13</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores13)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio13)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos com 12</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores12)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio12)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Acertos com 11</center></font></th>","utf8"))
                        self.wfile.write(bytes("<th bgcolor=\"#2E8B57\"><font color=\"#000000\"><center>Rateio</center></font></th>","utf8"))
                        self.wfile.write(bytes("</tr>", "utf8"))  
                        self.wfile.write(bytes("<tr>", "utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" + str(ganhadores11)+"</center></font></td>","utf8"))
                        self.wfile.write(bytes("<td bgcolor=\"#D3D3D3\"><font color=\"#000000\"><center>" +str(rateio11)+"</center></font></td>","utf8"))
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
    server_address = ('',666)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
