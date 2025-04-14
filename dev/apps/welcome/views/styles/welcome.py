from fasts.core.fastcss import css, render

# Define CSS styles for the welcome page
css(
    'body',
    background_color='#313131',
    font_family='Arial, sans-serif',
    display='flex',
    justify_content='center',
)

css(
    '#welcome',
    display='flex',
    flex_direction='column',
    justify_content='space-between',
    align_items='center',
    min_width='300px',
    max_width='40%',
    height='calc(100dvh - 100px)',
    text_align='center',
    padding_top='20px',
)
css('h1, h2, h3, h4, h5', color='#049688')
css('p', font_size='16px', line_height='1.5', color='#8C8C8C')
css('a', color='#049688', text_decoration='none')
css(
    'button',
    background_color='#049688',
    color='white',
    border='none',
    border_radius='5px',
    padding='10px 20px',
    cursor='pointer',
    font_size='16px',
)
css(
    '#footer p',
    font_size='1.2em',
    color='#049688',
    text_align='center',
    margin_top='20px'
)

welcome_css = render
