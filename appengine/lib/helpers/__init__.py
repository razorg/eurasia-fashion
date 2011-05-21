from main import jinja_dirs, jinja_env
import gettext, os
from gaesessions import get_current_session
import logging
class TemplatedRequest:
  def render_response(self, template, context=None):
    import os
    if context is None:
      return self.response.out.write(jinja_env.get_template(template).render())
    else:
      return self.response.out.write(jinja_env.get_template(template).render(context))
      
def IPNumToQuad(n,pad=3):
    "convert long int to dotted quad string paded with pad 0s"
    d = 256 * 256 * 256
    q = []
    while d > 0:
        m,n = divmod(n,d)
        q.append(str(m).rjust(pad,'0'))
        d = d/256
    return '.'.join(q)

def IPQuadToNum(ip):
    "convert decimal dotted quad string to long integer works with any number of padded 0s"
    hexn = ''.join(["%02X" % long(i) for i in ip.split('.')])
    return long(hexn, 16)

def IPencode(ip_address): # around 10% faster than IPQuadToNum
    return reduce((lambda ip, part: (ip << 8) | int(part)), ip_address.split('.'), 0)

def IPdecode(addr):
    return '.'.join(map(lambda (bits, ip): str((ip >> bits) & 255), [(i*8, addr) for i in range(4)])[::-1])

def gettext_en(x):
    return x

def translate(handler_method):
    def do(self, *args):
        #locale = self.request.get('lang')
        locale = get_current_session().get('lang')
        logging.debug(locale)
        if (not locale) or ((locale != 'en_US') and (locale != 'ru_RU')):
            locale = 'en_US'
        
        if locale == 'en_US':
            self._ = gettext_en
        else:
            self._ = gettext.translation('messages', os.path.join(os.path.dirname(__file__), '..', '..', 'babel'), [locale]).gettext
        jinja_env.install_gettext_callables(self._, None)
        handler_method(self, *args)
    return do
