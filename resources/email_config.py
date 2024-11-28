subject =  "Dein Wichtelpartner!"

def get_body(recipient_name, other_name):
    html_body = f"""\
    <html>
        <body>
            <p>Hallo <strong>{recipient_name}</strong>,</p>
            <p>das Los wurde gezogen! Dein Wichtelpartner ist: <strong>{other_name}</strong>.</p>
            <p>Ho Ho Ho!!</p>
            <p>Ich freue mich auf die Weihnchtsfeier,<br>
            der <em>DH34 Weihnachtsmann</em></p>
        </body>
    </html>
    """
    return html_body