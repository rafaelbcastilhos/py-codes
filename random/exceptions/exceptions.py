# -*- coding: utf-8 -*-
class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    def __init__(self, message="", saldo=None, valor=None):
        self.saldo = saldo
        self.valor = valor
        msg = "Saldo insuficiente para efetuar a transação\n"
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg)