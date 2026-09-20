const navButtons = [...document.querySelectorAll('.nav-button')];
const screens = [...document.querySelectorAll('.screen')];
const pointer = document.querySelector('.nav-pointer');
const actionBar = document.getElementById('actionBar');
const brandHome = document.getElementById('brandHome');
let selectedButton = navButtons.find(button => button.classList.contains('selected')) || navButtons[0];
let hoverButton = null;

function movePointer(button, instant = false) {
  if (!button || !pointer || !actionBar) return;
  const x = button.offsetLeft + (button.offsetWidth - pointer.offsetWidth) / 2;
  pointer.style.transitionDuration = instant ? '0ms' : '0.24s';
  pointer.style.setProperty('--pointer-x', `${x}px`);
}

function showScreen(name) {
  screens.forEach(screen => screen.classList.toggle('active', screen.id === `screen-${name}`));
}

function selectNavigation(button) {
  if (!button) return;
  selectedButton?.classList.remove('selected');
  selectedButton = button;
  selectedButton.classList.add('selected');
  navButtons.forEach(item => item.toggleAttribute('aria-current', item === selectedButton));
  showScreen(button.dataset.screen);
  if (!hoverButton) movePointer(selectedButton);
}

navButtons.forEach(button => {
  button.addEventListener('click', () => selectNavigation(button));
  button.addEventListener('mouseenter', () => {
    hoverButton = button;
    movePointer(button);
  });
  button.addEventListener('mouseleave', () => {
    if (hoverButton === button) hoverButton = null;
  });
  button.addEventListener('focus', () => {
    hoverButton = button;
    movePointer(button);
  });
  button.addEventListener('blur', () => {
    if (hoverButton === button) hoverButton = null;
    movePointer(selectedButton);
  });
});

actionBar?.addEventListener('mouseleave', () => {
  hoverButton = null;
  movePointer(selectedButton);
});

document.querySelectorAll('[data-goto]').forEach(element => {
  element.addEventListener('click', () => {
    const target = navButtons.find(button => button.dataset.screen === element.dataset.goto);
    if (target) selectNavigation(target);
  });
});

brandHome?.addEventListener('click', () => {
  const home = navButtons.find(button => button.dataset.screen === 'inicio');
  if (home) selectNavigation(home);
});

window.addEventListener('resize', () => movePointer(hoverButton || selectedButton, true));

async function chamarPython(nome, ...args) {
  if (window.pywebview && window.pywebview.api && typeof window.pywebview.api[nome] === 'function') {
    try {
      return await window.pywebview.api[nome](...args);
    } catch (error) {
      console.error(error);
      return null;
    }
  }
  return null;
}

function ativarPillGroup(grupo) {
  if (!grupo) return;
  const pills = [...grupo.querySelectorAll('.pill')];
  pills.forEach(pill => pill.addEventListener('click', () => {
    pills.forEach(item => item.classList.remove('selected'));
    pill.classList.add('selected');
    grupo.dataset.selected = pill.dataset.value;
  }));
  grupo.querySelector(`.pill[data-value="${grupo.dataset.selected}"]`)?.classList.add('selected');
}

ativarPillGroup(document.getElementById('formatoImagem'));
ativarPillGroup(document.getElementById('formatoMidia'));

let arquivoImagem = null;
const dropImagem = document.getElementById('dropImagem');
const nomeImagem = document.getElementById('imagemNomeArquivo');
const btnConverterImagem = document.getElementById('btnConverterImagem');
const statusImagem = document.getElementById('statusImagem');

async function escolherImagem() {
  const caminho = await chamarPython('selecionar_arquivo', 'imagem');
  if (!caminho) return;
  arquivoImagem = caminho;
  nomeImagem.textContent = caminho.split(/[\\/]/).pop();
  dropImagem.classList.add('has-file');
  btnConverterImagem.disabled = false;
  statusImagem.textContent = '';
}

if (dropImagem) {
  dropImagem.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    escolherImagem();
  });

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropImagem.addEventListener(eventName, e => {
      e.preventDefault();
      e.stopPropagation();
    });
  });

  ['dragenter', 'dragover'].forEach(eventName => {
    dropImagem.addEventListener(eventName, () => dropImagem.classList.add('drag-over'));
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropImagem.addEventListener(eventName, () => dropImagem.classList.remove('drag-over'));
  });

  dropImagem.addEventListener('drop', e => {
    const files = e.dataTransfer.files;
    if (files && files.length > 0) {
      const file = files[0];
      const caminho = file.path || file.name;
      if (caminho) {
        arquivoImagem = caminho;
        nomeImagem.textContent = file.name || caminho.split(/[\\/]/).pop();
        dropImagem.classList.add('has-file');
        btnConverterImagem.disabled = false;
        statusImagem.textContent = '';
      }
    }
  });
}

btnConverterImagem.addEventListener('click', async () => {
  if (!arquivoImagem) return;
  const formato = document.getElementById('formatoImagem').dataset.selected;
  btnConverterImagem.disabled = true;
  statusImagem.className = 'status-line';
  statusImagem.textContent = 'Convertendo...';
  const result = await chamarPython('converter_imagem_ui', arquivoImagem, formato);
  btnConverterImagem.disabled = false;
  if (result?.ok) {
    statusImagem.textContent = `Concluído: ${result.saida.split(/[\\/]/).pop()}`;
    statusImagem.className = 'status-line ok';
  } else {
    statusImagem.textContent = result?.erro || 'Não foi possível conectar ao backend.';
    statusImagem.className = 'status-line error';
  }
});

let arquivoMidia = null;
const dropMidia = document.getElementById('dropMidia');
const nomeMidia = document.getElementById('midiaNomeArquivo');
const btnConverterMidia = document.getElementById('btnConverterMidia');
const statusMidia = document.getElementById('statusMidia');

async function escolherMidia() {
  const caminho = await chamarPython('selecionar_arquivo', 'midia');
  if (!caminho) return;
  arquivoMidia = caminho;
  nomeMidia.textContent = caminho.split(/[\\/]/).pop();
  dropMidia.classList.add('has-file');
  btnConverterMidia.disabled = false;
  statusMidia.textContent = '';
}

if (dropMidia) {
  dropMidia.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    escolherMidia();
  });

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropMidia.addEventListener(eventName, e => {
      e.preventDefault();
      e.stopPropagation();
    });
  });

  ['dragenter', 'dragover'].forEach(eventName => {
    dropMidia.addEventListener(eventName, () => dropMidia.classList.add('drag-over'));
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropMidia.addEventListener(eventName, () => dropMidia.classList.remove('drag-over'));
  });

  dropMidia.addEventListener('drop', e => {
    const files = e.dataTransfer.files;
    if (files && files.length > 0) {
      const file = files[0];
      const caminho = file.path || file.name;
      if (caminho) {
        arquivoMidia = caminho;
        nomeMidia.textContent = file.name || caminho.split(/[\\/]/).pop();
        dropMidia.classList.add('has-file');
        btnConverterMidia.disabled = false;
        statusMidia.textContent = '';
      }
    }
  });
}

btnConverterMidia.addEventListener('click', async () => {
  if (!arquivoMidia) return;
  const formato = document.getElementById('formatoMidia').dataset.selected;
  btnConverterMidia.disabled = true;
  statusMidia.className = 'status-line';
  statusMidia.textContent = 'Convertendo...';
  const result = await chamarPython('converter_midia_ui', arquivoMidia, formato);
  btnConverterMidia.disabled = false;
  if (result?.ok) {
    statusMidia.textContent = `Concluído: ${result.saida.split(/[\\/]/).pop()}`;
    statusMidia.className = 'status-line ok';
  } else {
    statusMidia.textContent = result?.erro || 'Não foi possível conectar ao backend.';
    statusMidia.className = 'status-line error';
  }
});

const urlDownload = document.getElementById('urlDownload');
const toggleAudio = document.getElementById('toggleAudio');
const btnPasta = document.getElementById('btnPasta');
const pastaTexto = document.getElementById('pastaTexto');
const btnBaixar = document.getElementById('btnBaixar');
const statusDownload = document.getElementById('statusDownload');
let pastaDestino = null;

toggleAudio.addEventListener('click', () => {
  const current = toggleAudio.getAttribute('aria-checked') === 'true';
  toggleAudio.setAttribute('aria-checked', String(!current));
});

btnPasta.addEventListener('click', async () => {
  const pasta = await chamarPython('selecionar_pasta');
  if (!pasta) return;
  pastaDestino = pasta;
  pastaTexto.textContent = pasta;
});

btnBaixar.addEventListener('click', async () => {
  const url = urlDownload.value.trim();
  if (!url) {
    statusDownload.textContent = 'Informe uma URL antes de baixar.';
    statusDownload.className = 'status-line error';
    return;
  }
  const soAudio = toggleAudio.getAttribute('aria-checked') === 'true';
  btnBaixar.disabled = true;
  statusDownload.className = 'status-line';
  statusDownload.textContent = 'Baixando...';

  const result = await chamarPython('baixar_midia_ui', url, pastaDestino, soAudio);
  btnBaixar.disabled = false;

  if (result?.ok) {
    statusDownload.textContent = 'Download concluído!';
    statusDownload.className = 'status-line ok';
  } else {
    statusDownload.textContent = result?.erro || 'Erro ao realizar download.';
    statusDownload.className = 'status-line error';
  }
});

window.addEventListener('pywebviewready', async () => {
  if (!pastaDestino) {
    const padrao = await chamarPython('caminho_padrao');
    if (padrao && pastaTexto) {
      pastaTexto.textContent = padrao;
    }
  }
});

requestAnimationFrame(() => movePointer(selectedButton, true));