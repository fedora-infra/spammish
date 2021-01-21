# -*- mode: ruby -*-
# vi: set ft=ruby :
ENV['VAGRANT_NO_PARALLEL'] = 'yes'

Vagrant.configure(2) do |config|
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true


  config.vm.define "freeipa" do |freeipa|
    freeipa.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/32/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-32-1.6.x86_64.vagrant-libvirt.box"
    freeipa.vm.box = "f32-cloud-libvirt"
    freeipa.vm.hostname = "ipa.spammish.test"
    freeipa.hostmanager.aliases = ("kerberos.example.test")

    freeipa.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = 2048
    end

    # Vagrant adds '127.0.0.1 ipa.example.test ipa' as the first line in /etc/hosts
    # and freeipa doesnt like that, so we remove it
    freeipa.vm.provision "shell", inline: "sudo sed -i '1d' /etc/hosts"

    freeipa.vm.provision "ansible" do |ansible|
      ansible.playbook = "devel/ansible/freeipa.yml"
    end
  end

  config.vm.define "spammish" do |spammish|
    spammish.vm.box_url = "https://download.fedoraproject.org/pub/fedora/linux/releases/32/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-32-1.6.x86_64.vagrant-libvirt.box"
    spammish.vm.box = "f32-cloud-libvirt"
    spammish.vm.hostname = "spammish.spammish.test"

    spammish.vm.synced_folder ".", "/home/vagrant/spammish", type: "sshfs"

    spammish.vm.provider :libvirt do |libvirt|
      libvirt.cpus = 2
      libvirt.memory = 2048
    end

    spammish.vm.provision "ansible" do |ansible|
      ansible.playbook = "devel/ansible/spammish.yml"
      ansible.verbose = true
    end
  end

end
