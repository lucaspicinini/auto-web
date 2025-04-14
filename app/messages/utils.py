from datetime import datetime

from app.open_cart.order import Order


class Utils():
    """Global utils."""

    @staticmethod
    def generate_logistic_msg(
        order: Order,
        authorization_post_code: str | None,
        date: datetime,
        expire_date: datetime,
    ) -> str:
        """
        Returns a message with the reverse logistic information.
        """
        return f"""
Olá {order.firstname},

Segue um código de postagem para que nada lhe seja cobrado na agência dos correios ao nos retornar a encomenda:

- Código da Autorização de Postagem: {authorization_post_code}
- Emitido em: {date.strftime("%d/%m/%Y")}
- Data de Validade: {expire_date.strftime("%d/%m/%Y")}
- Serviço de Encomenda: {order.service}
- Remetente autorizado: {order.fullname}
- Quantidade de objetos: 1

- Para utilizá-la, o consumidor dever se dirigir a uma
Agência Própria ou Franqueada dos Correios, levando
consigo, obrigatoriamente, o Código de Autorização e o
objeto para postagem.

- Caso esta Autorização de Postagem inclua a aquisição de
embalagem, importante orientar o consumidor de que a postagem
com fornecimento de embalagem somente pode ser efetuada em
uma Agência Própria (AC). Alternativamente, se concordar, a
postagem pode ser realizada em uma Agência Franqueada (AGF)
mediante o pagamento da embalagem correspondente pelo próprio
cliente.

DESTINATÁRIO:
REXPEITA
Rua Campanário 31 , Brás de Pina
Rio de Janeiro - RJ
CEP: 21235-800

Assim que o item chegar em nossa matriz ou que você nos informar por aqui que a postagem já foi concluída, vamos efetuar sua troca ou devolução. Agradecemos muito por confiar em nossa marca e aguardamos seu retorno.

Atenciosamente, Rexpeita.
"""
