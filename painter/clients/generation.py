from rudalle import get_rudalle_model, get_tokenizer, get_vae
from rudalle.pipelines import generate_images, show
from rudalle.utils import seed_everything


def start(text):
    device = 'cpu'
    tokenizer = get_tokenizer()
    dalle = get_rudalle_model(
        'Malevich',
        pretrained=True,
        fp16=False,
        device=device,
        cache_dir='models/rudalle',
    )
    vae = get_vae().to(device)

    pil_images = []
    scores = []

    seed_everything(42)  # noqa: WPS432
    top_k, top_p = 1024, 0.8
    images_num = 1

    _pil_images, _scores = generate_images(
        text,
        tokenizer,
        dalle,
        vae,
        top_k=top_k,
        images_num=images_num,
        top_p=top_p,
        bs=4,
    )
    pil_images += _pil_images
    scores += _scores
    show(pil_images, 6, save_dir='.data/pics')


def main():
    start('крыса на окне')


if __name__ == '__main__':
    main()
