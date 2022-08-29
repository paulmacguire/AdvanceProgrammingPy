from servidor_archivo import Servidor
import sys

if __name__ == "__main__":
    server = Servidor()
    
    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(82, "+") + "\n")
    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(82, "-"))
        print("".center(82, "-") + "\n")
        server.socket_servidor.close()
        sys.exit()
