# nomad-aws
nomad cluster following [nomad architecture reference](https://learn.hashicorp.com/tutorials/nomad/production-reference-architecture-vm-with-consul?in=nomad/enterprise)

## Diagram
![](./diagram/nomad-aws-diagram.png)

## How to use this repo
- Clone this repo
```
git clone https://github.com/ion-onboarding/nomad-aws.git
```

- change directory
```
cd nomad-aws
```

## Todo


## Done
- [x] This README
- [x] Diagram
- [x] create `nomad-aws/manually/infrastructure/README.md`
- [x] in `README.md` add manual steps to create components described in the diagram
- [x] test VMs can ping internet and each other
- [x] adjust region to reflect Nomad region and datacenter
- [x] add link to diagram to main README and ./manually/infrastructure/README
- [x] manual-installation: create branch manual-installation and add Todo list
- [x] manual-installation: create `manually/installation/README.md` structure
- [x] manual-installation: consul install on machines `consul-server`, `nomad-server` and `nomad-client`
- [x] manual-installation: add consul systemD service file on machines `consul-server`, `nomad-server` and `nomad-client`
- [x] manual-installation: add nomad systemD service file on machines `nomad-server` and `nomad-client`
- [x] manual-installation: configure consul agent to run in server mode on `consul-server` machine
- [x] manual-installation: configure consul agent to run in client mode on `nomad-server` and `nomad-client` machines
- [x] manual-installation: configure nomad agent to run in server mode on `nomad-server`
- [x] manual-installation: configure nomad agent to run in client mode on `nomad-client`
- [x] manual-installation: install docker on `nomad-client`
- [x] manual-installation: install envoy on `nomad-client`
