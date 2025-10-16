import vagrant
import os

# Caminho da pasta onde o Vagrant vai rodar
CAMINHO_VAGRANT = r"C:\Users\letic\VmAutomatic"

# Cria a pasta se não existir
os.makedirs(CAMINHO_VAGRANT, exist_ok=True)

# Cria um arquivo Vagrantfile básico se não existir
vagrantfile_path = os.path.join(CAMINHO_VAGRANT, "Vagrantfile")
if not os.path.exists(vagrantfile_path):
    with open(vagrantfile_path, "w") as f:
        f.write("""
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"   # Ubuntu 18.04 básico
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 1
  end
end
""")

# Inicializa o Vagrant
v = vagrant.Vagrant(root=CAMINHO_VAGRANT)

print("== Listando VMs atuais... ==")
status = v.status()
if status:
    for vm in status:
        print(f" - {vm.name}: {vm.state}")
else:
    print("Nenhuma VM encontrada.")

print("\n== Criando e iniciando nova VM automaticamente... ==")
v.up()

print("== VM criada e em execução! ==")

print("\n== Verificando status atual: ==")
status = v.status()
for vm in status:
    print(f" - {vm.name}: {vm.state}")

print("\n== IP (configuração SSH) da VM: ==")
print(v.ssh_config())

print("\n== Para desligar a VM depois, execute manualmente: vagrant halt ==")
