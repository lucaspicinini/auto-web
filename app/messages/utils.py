class Utils():
    """Global utils."""

    @staticmethod
    def generate_logistic_msg(
        firstname: str | None,
        fullname: str,
        authorization_post_code: str | None,
        date: str,
        expire_date: str,
        service: str
    ) -> str:
        """
        Returns a message with the reverse logistic information.
        """
        return f"""
Olá {firstname},

Segue um código de postagem para que nada lhe seja cobrado na agência
dos correios ao nos retornar a encomenda:

- Código da Autorização de Postagem: {authorization_post_code}
- Emitido em: {date}
- Data de Validade: {expire_date}
- Serviço de Encomenda: {service}
- Remetente autorizado: {fullname}
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

Assim que o item chegar em nossa matriz ou que você nos informar
por aqui que a postagem já foi efetuada, vamos efetuar sua troca
ou devolução. Agrademos muito por confiar em nossa marca e aguardamos
seu retorno.

Atenciosamente, Rexpeita.
"""
