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

            url = 'https://www.lotodicas.com.br/api/mega-sena'

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

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<center><h1>Concurso: " +
                                   str(numeroConcurso)+"</h1></center>", "utf8"))

            self.wfile.write(bytes("<center><h1>Acumulado: " +
                                   str(acumulado).upper()+"</h1></center>", "utf8"))
            self.wfile.write(bytes("<center><h1>Data: " +
                                   str(dataConcurso)+"</h1></center>", "utf8"))
            self.wfile.write(bytes("<center><h1>Dezenas Sorteadas " +
                                   str(dezenasSorteadas)+"</h1></center>", "utf8"))

            if len(apostasCom6) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 6 acertos</h3></center>", "utf8"))
                for aposta in apostasCom6:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom5) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 5 acertos</h3></center>", "utf8"))
                for aposta in apostasCom5:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom4) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 4 acertos</h3></center>", "utf8"))
                for aposta in apostasCom4:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom3) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 3 acertos</h3></center>", "utf8"))
                for aposta in apostasCom3:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom2) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 2 acertos</h3></center>", "utf8"))
                for aposta in apostasCom2:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom1) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 1 acertos</h3></center>", "utf8"))
                for aposta in apostasCom1:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            if len(apostasCom0) > 0:
                self.wfile.write(
                    bytes("<center><h3>Apostas com 0 acertos</h3></center>", "utf8"))
                for aposta in apostasCom0:
                    matches = set(dezenasSorteadas) & set(aposta)
                    numberOfMatched = len(matches)
                    self.wfile.write(bytes("<center><p>", "utf8"))
                    if numberOfMatched >= 4:
                        self.wfile.write(
                            bytes("<font color=""green"">", "utf8"))
                    self.wfile.write(bytes("Jogo "+str(aposta)+" Matches: " +
                                           str(matches)+" QtdAcertos: "+str(numberOfMatched), "utf8"))
                    self.wfile.write(bytes("</font>", "utf8"))
                    self.wfile.write(bytes("</p></center>", "utf8"))
            self.wfile.write(bytes("<center><h2>Acertos na Sena: " +
                                   str(ganhadores[0])+" Rateio: R$"+str(rateio[0])+"</h2></center>", "utf8"))
            self.wfile.write(bytes("<center><h2>Acertos na Quina: " +
                                   str(ganhadores[1])+" Rateio: R$"+str(rateio[1])+"</h2></center>", "utf8"))
            self.wfile.write(bytes("<center><h2>Acertos na Quadra: " +
                                   str(ganhadores[2])+" Rateio: R$"+str(rateio[2])+"</h2></center>", "utf8"))
            self.wfile.write(bytes("<center><h1>Proximo Concurso: " +
                                   str(proximaData)+"</h1></center>", "utf8"))
            self.wfile.write(bytes("<center><h1>Valor Estimado: R$" +
                                   str(proximaEstimativa)+"</h1></center>", "utf8"))

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
