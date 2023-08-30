from Classes.aluno import Aluno
from Classes.contas_a_pagar import Contas_a_pagar
from Classes.eletrodomestico import Eletrodomestico
from Classes.funcionario import Funcionario
from Classes.pagamento import Pagamento
from Classes.pessoa import Pessoa
from Classes.produto import Produto
from Classes.smartphone import Smartphone
from Classes.veiculo import Veículo

aluno1 = Aluno(12345678, 'Matheus Strapasson', 17, 'Info22', 'Marinês Strapasson')
conta1 = Contas_a_pagar.get_bill_info()
eletrodomestico1 = Eletrodomestico.get_info()
funcionario1 = Funcionario()
pagamento1 = Pagamento(12345678, '10/02/2022', 'Matheus Strapasson', 'Ronan Silva', 4000.96)
pessoa1 = Pessoa('Matheus Strapasson', 17, 'M', 182, 78, '126133782', '09135052937')
produto1 = Produto()
smartphone1 = Smartphone.get_smartphone_info()
veiculo1 = Veículo('Carro', 'Chevrolet', 'Camaro', '2007', 'ABC1D234')

print('\nAluno:\n',aluno1)
print('\nConta:\n',conta1)
print('\nEletrodoméstico:\n',eletrodomestico1)
print('\nFuncionário:\n',funcionario1)
print('\nPagamento:\n',pagamento1)
print('\nPessoa:\n', pessoa1)
print('\nProduto:\n',produto1)
print('\nSmartphone:\n',smartphone1)
print('\nVeículo:\n',veiculo1)