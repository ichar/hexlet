import sys
import os
import re


##  =========================================================================================================  ##

def _pout(s, **kw):
    if not is_v3:
        print(s, end='end' in kw and kw.get('end') or None)
        if 'flush' in kw and kw['flush'] == True:
            sys.stdout.flush()
    else:
        print(s, **kw)

class Logger():
    
    def __init__(self, to_file=None, encoding=default_unicode, mode='w+', bom=True, end_of_line=EOL):
        self.is_to_file = to_file and 1 or 0
        self.encoding = encoding
        self.fo = None
        self.end_of_line = end_of_line

        if IsDisableOutput and to_file:
            pass
        elif to_file:
            self.fo = codecs.open(to_file, encoding=self.encoding, mode=mode)
            if bom:
                self.fo.write(codecs.BOM_UTF8.decode(self.encoding))
            self.out(to_file, console_forced=True) #_pout('--> %s' % to_file)
        else:
            pass

    def get_to_file(self):
        return self.fo

    def set_default_encoding(self, encoding=default_unicode):
        if sys.getdefaultencoding() == 'ascii':
            reload(sys)
            sys.setdefaultencoding(encoding)
        _pout('--> %s' % sys.getdefaultencoding())

    def out(self, line, console_forced=False, without_decoration=False):
        if not line:
            return
        elif console_forced or not (self.fo or self.is_to_file):
            mask = '%s' % (not without_decoration and '--> ' or '')
            try:
                _pout('%s%s' % (mask, line))
            except:
                if is_v3:
                    pass
                elif type(line) is UnicodeType:
                    v = ''
                    for x in line:
                        try:
                            _pout(x, end='')
                            v += x.encode(default_encoding, 'ignore')
                        except:
                            v += '?'
                    _pout('')
                else:
                    _pout('%s%s' % (mask, line.decode(default_encoding, 'ignore')))
        elif IsDisableOutput:
            return
        else:
            if type(line) in StringTypes:
                try:
                    self.fo.write(line)
                except:
                    if is_v3:
                        return
                    try:
                        self.fo.write(unicode(line, self.encoding))
                    except:
                        try:
                            self.fo.write(line.decode(default_encoding)) #, 'replace'
                        except:
                            raise
                if not line == self.end_of_line:
                    self.fo.write(self.end_of_line)

    def progress(self, line=None, mode='continue'):
        if mode == 'start':
            _pout('--> %s:' % (line or ''), end=' ')
        elif mode == 'end':
            _pout('', end='\n')
        else:
            _pout('#', end='', flush=True)

    def close(self):
        if IsDisableOutput:
            return
        if not self.fo:
            return
        self.fo.close()
