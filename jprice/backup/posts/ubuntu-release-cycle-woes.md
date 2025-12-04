I've learned a hard lesson about Ubuntu's release cycle that I want to share to save others the headache I put myself through. If you've ever spun up an Ubuntu server on a cloud provider like DigitalOcean and then a few months later found that your apt package manager is broken and you can't update or install anything, you already know the annoyance I'm talking about. Ubuntu's release cycle is predictable on paper, but the real world consequences can catch you off guard if you're not fully aware of how it works.

Canonical cuts a release every 6 months an April and October. The April release of every even numbered year is marked as Long Term Support (LTS), meaning it will receive updates and support for 5 years. The October releases, and the April releases of odd numbered years are marked as Interim releases, meaning they only receive updates and support for 9 months.

The interim releases are where the problem starts.

## The Problem

Once an interim release reaches its end of life (EOL), it's package repositories are removed from the main mirrors, causing apt to break. This means that if you happen to be using an interim release when it hits EOL, you'll find yourself unable to update or install packages. To fix this, you have to manually change your apt sources to point to the old-releases repository, which does not provide security patches. This is a temporary fix, but it means you're now running an unsupported system.

> Okay, so can I just downgrade to the last LTS release?

**Nope!** Ubuntu does not support downgrading releases. The only supported path is to upgrade to the next release. So if you're on an interim release that has reached EOL, you have to upgrade to the next interim release, which will also reach EOL in 9 months, forcing you to repeat the process again. And then, after that, the **NEXT** release is **ALSO** an interim release, meaning you'll have to do this dance yet again in another 9 months. Finally after this the next release will be the LTS release, which you can then upgrade to and finally be on a stable 5 year support cycle.

So, if you're not aware of this release cycle and just picked the latest Ubuntu release when spinning up a VM, and it happens to be an interim release, you may find yourself stuck in a cycle of short-lived versions: upgrade every nine months or watch apt break again. Rebuilding and migrating your entire infrastructure to an LTS release is your ony other option.

The frustrating part? Cloud providers tend to default to the newest Ubuntu version available, even if it's an interim release. No warning, no explanation, just the latest version. _Luckily_ for me, I did this **three times** for my personal droplets before I realized what was going on.

## My Takeaway

I will not be using an Ubuntu VM for any personal production servers again, even an LTS release. I will spend the extra 15 minutes to set up Debian instead, and enjoy the stability and long term support of it's release cycle. Lesson learned. If you're using Ubuntu for production, make sure you're always on an LTS release to avoid these headaches.
