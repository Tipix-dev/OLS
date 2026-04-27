FROM archlinux:latest

RUN sudo pacman -Syu && \
sudo pacman -S --noconfirm  wget tar make curl


RUN curl -sSL https://raw.githubusercontent.com/Tipix-dev/OLS/main/install.sh | bash

WORKDIR /app

CMD ["bash", "-l"]
