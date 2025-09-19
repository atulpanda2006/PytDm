#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyDM - Python Download Manager
Interface graphique de téléchargement avec tkinter
Fonctionnalités: pause/reprendre, sélection de dossier, barre de progression

Author: Docteur-Parfait
Repository: https://github.com/Docteur-Parfait/pydm
License: MIT
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import os
import threading
import time
from urllib.parse import urlparse
from pathlib import Path
import subprocess
import platform

class DownloadManager:
    def __init__(self):
        self.download_thread = None
        self.is_paused = False
        self.is_cancelled = False
        self.downloaded_size = 0
        self.total_size = 0
        self.file_path = None
        self.response = None
        self.session = requests.Session()  # Session pour maintenir les cookies

class DownloadGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyDM - Python Download Manager")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)  # Taille minimale
        self.root.resizable(True, True)
        
        # Style
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.download_manager = DownloadManager()
        self.download_folder = tk.StringVar(value=str(Path.home() / "Downloads"))
        
        self.setup_ui()
        self.reset_buttons()  # Initialiser l'état des boutons
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        
        # Créer un Canvas et une Scrollbar pour le scroll
        canvas = tk.Canvas(self.root, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Titre principal
        title_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="PyDM - Python Download Manager", 
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack()
        
        # Frame principal
        main_frame = tk.Frame(scrollable_frame, bg='#f0f0f0')
        main_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Section URL
        url_frame = tk.LabelFrame(main_frame, text="🔗 URL du fichier", font=('Arial', 10, 'bold'), bg='#f0f0f0')
        url_frame.pack(fill='x', pady=(0, 15))
        
        self.url_entry = tk.Entry(url_frame, font=('Arial', 10))
        self.url_entry.pack(pady=10, padx=10, fill='x')
        self.url_entry.bind('<Return>', lambda e: self.start_download())
        
        # Section dossier de téléchargement
        folder_frame = tk.LabelFrame(main_frame, text="📁 Dossier de téléchargement", font=('Arial', 10, 'bold'), bg='#f0f0f0')
        folder_frame.pack(fill='x', pady=(0, 15))
        
        folder_inner_frame = tk.Frame(folder_frame, bg='#f0f0f0')
        folder_inner_frame.pack(fill='x', pady=10, padx=10)
        
        self.folder_entry = tk.Entry(folder_inner_frame, textvariable=self.download_folder, font=('Arial', 9))
        self.folder_entry.pack(side='left', fill='x', expand=True)
        
        browse_btn = tk.Button(
            folder_inner_frame, 
            text="📂 Parcourir", 
            command=self.browse_folder,
            bg='#3498db',
            fg='white',
            font=('Arial', 8, 'bold'),
            relief='flat',
            padx=10
        )
        browse_btn.pack(side='right', padx=(5, 0))
        
        # Section nom du fichier
        filename_frame = tk.LabelFrame(main_frame, text="📄 Nom du fichier", font=('Arial', 10, 'bold'), bg='#f0f0f0')
        filename_frame.pack(fill='x', pady=(0, 15))
        
        self.filename_entry = tk.Entry(filename_frame, font=('Arial', 10))
        self.filename_entry.pack(pady=10, padx=10, fill='x')
        
        # Section progression
        progress_frame = tk.LabelFrame(main_frame, text="📊 Progression", font=('Arial', 10, 'bold'), bg='#f0f0f0')
        progress_frame.pack(fill='x', pady=(0, 15))
        
        # Barre de progression
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            variable=self.progress_var, 
            maximum=100,
            mode='determinate'
        )
        self.progress_bar.pack(pady=15, padx=10, fill='x')
        
        # Labels d'information
        self.status_label = tk.Label(
            progress_frame, 
            text="Prêt à télécharger", 
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.status_label.pack(pady=(0, 5))
        
        self.speed_label = tk.Label(
            progress_frame, 
            text="", 
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.speed_label.pack()
        
        # Boutons de contrôle - Frame principal
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=15)
        
        # Frame pour les boutons de gauche (télécharger, pause, annuler)
        left_buttons_frame = tk.Frame(button_frame, bg='#f0f0f0')
        left_buttons_frame.pack(side='left', fill='x', expand=True)
        
        # Frame pour les boutons de droite (ouvrir dossier)
        right_buttons_frame = tk.Frame(button_frame, bg='#f0f0f0')
        right_buttons_frame.pack(side='right')
        
        # Bouton télécharger
        self.download_btn = tk.Button(
            left_buttons_frame,
            text="🚀 Télécharger",
            command=self.start_download,
            bg='#27ae60',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=6
        )
        self.download_btn.pack(side='left', padx=(0, 5), fill='x', expand=True)
        
        # Bouton pause/reprendre
        self.pause_btn = tk.Button(
            left_buttons_frame,
            text="⏸️ Pause",
            command=self.toggle_pause,
            bg='#f39c12',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=6,
            state='disabled'
        )
        self.pause_btn.pack(side='left', padx=(0, 5), fill='x', expand=True)
        
        # Bouton annuler
        self.cancel_btn = tk.Button(
            left_buttons_frame,
            text="❌ Annuler",
            command=self.cancel_download,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=6,
            state='disabled'
        )
        self.cancel_btn.pack(side='left', padx=(0, 5), fill='x', expand=True)
        
        # Bouton ouvrir dossier
        self.open_folder_btn = tk.Button(
            right_buttons_frame,
            text="📂 Ouvrir Dossier",
            command=self.open_download_folder,
            bg='#9b59b6',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='flat',
            padx=15,
            pady=6
        )
        self.open_folder_btn.pack(side='right')
        
        # Pack du canvas et de la scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind la molette de la souris au canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Bind la molette sur Linux
        def _on_mousewheel_linux(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<Button-4>", _on_mousewheel_linux)
        canvas.bind_all("<Button-5>", _on_mousewheel_linux)
        
        # Gérer le redimensionnement de la fenêtre
        def on_window_resize(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        self.root.bind('<Configure>', on_window_resize)
        
        # Stocker les références pour le nettoyage
        self.canvas = canvas
        self.scrollbar = scrollbar
        
    def browse_folder(self):
        """Ouvre le dialogue de sélection de dossier"""
        folder = filedialog.askdirectory(initialdir=self.download_folder.get())
        if folder:
            self.download_folder.set(folder)
    
    def get_filename_from_url(self, url):
        """Extrait le nom du fichier à partir de l'URL"""
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            filename = "fichier_telecharge"
        
        return filename
    
    def update_progress(self, downloaded, total, speed=0):
        """Met à jour la barre de progression et les labels"""
        if total > 0:
            percentage = (downloaded / total) * 100
            self.progress_var.set(percentage)
            
            # Formatage des tailles
            downloaded_mb = downloaded / (1024 * 1024)
            total_mb = total / (1024 * 1024)
            
            status_text = f"Téléchargé: {downloaded_mb:.2f} MB / {total_mb:.2f} MB ({percentage:.1f}%)"
            self.status_label.config(text=status_text)
            
            if speed > 0:
                speed_text = f"Vitesse: {speed:.2f} MB/s"
                self.speed_label.config(text=speed_text)
    
    def reset_buttons(self):
        """Réinitialise l'état des boutons"""
        self.download_btn.config(state='normal')
        self.pause_btn.config(state='disabled')
        self.cancel_btn.config(state='disabled')
        self.progress_var.set(0)
        self.status_label.config(text="Prêt à télécharger")
        self.speed_label.config(text="")

    def start_download(self):
        """Démarre le téléchargement"""
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL valide")
            return
        
        if not url.startswith(('http://', 'https://')):
            messagebox.showerror("Erreur", "L'URL doit commencer par http:// ou https://")
            return
        
        # Désactiver les boutons
        self.download_btn.config(state='disabled')
        self.pause_btn.config(state='normal')
        self.cancel_btn.config(state='normal')
        
        # Réinitialiser les variables
        self.download_manager.is_paused = False
        self.download_manager.is_cancelled = False
        self.download_manager.downloaded_size = 0
        
        # Démarrer le téléchargement dans un thread séparé
        self.download_manager.download_thread = threading.Thread(target=self.download_file)
        self.download_manager.download_thread.daemon = True
        self.download_manager.download_thread.start()
    
    def get_headers(self):
        """Retourne les en-têtes HTTP pour simuler un navigateur"""
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }

    def download_file(self):
        """Fonction de téléchargement dans un thread séparé"""
        try:
            url = self.url_entry.get().strip()
            headers = self.get_headers()
            
            # Obtenir les informations du fichier
            self.root.after(0, lambda: self.status_label.config(text="🔍 Vérification du fichier..."))
            
            head_response = self.download_manager.session.head(url, headers=headers, allow_redirects=True, timeout=10)
            head_response.raise_for_status()
            
            self.download_manager.total_size = int(head_response.headers.get('content-length', 0))
            
            if self.download_manager.total_size == 0:
                self.root.after(0, lambda: self.status_label.config(text="⚠️ Taille inconnue - téléchargement sans progression"))
                self.download_without_progress(url)
                return
            
            # Obtenir le nom du fichier
            filename = self.filename_entry.get().strip()
            if not filename:
                content_disposition = head_response.headers.get('content-disposition', '')
                if 'filename=' in content_disposition:
                    filename = content_disposition.split('filename=')[1].strip('"')
                else:
                    filename = self.get_filename_from_url(url)
            
            # Chemin complet du fichier
            self.download_manager.file_path = os.path.join(self.download_folder.get(), filename)
            
            # Vérifier si le fichier existe déjà (pour reprendre)
            resume_pos = 0
            if os.path.exists(self.download_manager.file_path):
                resume_pos = os.path.getsize(self.download_manager.file_path)
                if resume_pos < self.download_manager.total_size:
                    self.root.after(0, lambda: self.status_label.config(text=f"📥 Reprise du téléchargement à {resume_pos / (1024*1024):.2f} MB"))
                else:
                    self.root.after(0, lambda: self.status_label.config(text="✅ Fichier déjà téléchargé"))
                    self.download_complete()
                    return
            
            # Téléchargement avec reprise
            self.download_with_resume(url, resume_pos)
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                self.root.after(0, lambda: self.show_error("❌ Accès interdit (403 Forbidden)\n\nLe serveur bloque les téléchargements automatiques.\nEssayez de copier le lien directement depuis votre navigateur."))
            elif e.response.status_code == 404:
                self.root.after(0, lambda: self.show_error("❌ Fichier non trouvé (404)\n\nVérifiez que l'URL est correcte."))
            else:
                self.root.after(0, lambda: self.show_error(f"❌ Erreur HTTP {e.response.status_code}: {str(e)}"))
        except requests.exceptions.RequestException as e:
            self.root.after(0, lambda: self.show_error(f"❌ Erreur de connexion: {str(e)}"))
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"❌ Erreur inattendue: {str(e)}"))
    
    def download_with_resume(self, url, resume_pos):
        """Téléchargement avec possibilité de reprise"""
        headers = self.get_headers()
        if resume_pos > 0:
            headers['Range'] = f'bytes={resume_pos}-'
        
        response = self.download_manager.session.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        self.download_manager.response = response
        
        mode = 'ab' if resume_pos > 0 else 'wb'
        downloaded = resume_pos
        start_time = time.time()
        last_update = start_time
        
        with open(self.download_manager.file_path, mode) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if self.download_manager.is_cancelled:
                    break
                
                # Gestion de la pause
                while self.download_manager.is_paused and not self.download_manager.is_cancelled:
                    time.sleep(0.1)
                
                if self.download_manager.is_cancelled:
                    break
                
                if chunk:
                    file.write(chunk)
                    downloaded += len(chunk)
                    self.download_manager.downloaded_size = downloaded
                    
                    # Mise à jour de l'interface (limiter la fréquence)
                    current_time = time.time()
                    if current_time - last_update >= 0.1:  # Mise à jour toutes les 100ms
                        speed = (downloaded - resume_pos) / (current_time - start_time) / (1024 * 1024)
                        self.root.after(0, lambda: self.update_progress(downloaded, self.download_manager.total_size, speed))
                        last_update = current_time
        
        if not self.download_manager.is_cancelled:
            self.root.after(0, self.download_complete)
        else:
            self.root.after(0, self.download_cancelled)
    
    def download_without_progress(self, url):
        """Téléchargement sans barre de progression (taille inconnue)"""
        try:
            headers = self.get_headers()
            response = self.download_manager.session.get(url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            
            filename = self.filename_entry.get().strip()
            if not filename:
                filename = self.get_filename_from_url(url)
            
            self.download_manager.file_path = os.path.join(self.download_folder.get(), filename)
            
            with open(self.download_manager.file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if self.download_manager.is_cancelled:
                        break
                    
                    while self.download_manager.is_paused and not self.download_manager.is_cancelled:
                        time.sleep(0.1)
                    
                    if self.download_manager.is_cancelled:
                        break
                    
                    if chunk:
                        file.write(chunk)
            
            if not self.download_manager.is_cancelled:
                self.root.after(0, self.download_complete)
            else:
                self.root.after(0, self.download_cancelled)
                
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"Erreur: {str(e)}"))
    
    def toggle_pause(self):
        """Bascule entre pause et reprise"""
        if self.download_manager.is_paused:
            self.download_manager.is_paused = False
            self.pause_btn.config(text="⏸️ Pause")
            self.status_label.config(text="▶️ Reprise du téléchargement...")
        else:
            self.download_manager.is_paused = True
            self.pause_btn.config(text="▶️ Reprendre")
            self.status_label.config(text="⏸️ Téléchargement en pause...")
    
    def cancel_download(self):
        """Annule le téléchargement"""
        self.download_manager.is_cancelled = True
        self.download_manager.is_paused = False
        
        # Supprimer le fichier partiellement téléchargé
        if self.download_manager.file_path and os.path.exists(self.download_manager.file_path):
            try:
                os.remove(self.download_manager.file_path)
            except:
                pass
        
        self.download_cancelled()
    
    def download_complete(self):
        """Appelé quand le téléchargement est terminé"""
        self.status_label.config(text="✅ Téléchargement terminé!")
        self.speed_label.config(text="")
        self.progress_var.set(100)
        
        # Réactiver les boutons
        self.reset_buttons()
        
        # Message de succès
        messagebox.showinfo("Succès", f"Fichier téléchargé avec succès!\n\nEmplacement: {self.download_manager.file_path}")
    
    def download_cancelled(self):
        """Appelé quand le téléchargement est annulé"""
        self.status_label.config(text="❌ Téléchargement annulé")
        self.speed_label.config(text="")
        
        # Réactiver les boutons
        self.reset_buttons()
    
    def show_error(self, message):
        """Affiche une erreur"""
        self.status_label.config(text=f"❌ {message}")
        self.speed_label.config(text="")
        
        # Réactiver les boutons
        self.reset_buttons()
        
        messagebox.showerror("Erreur", message)
    
    def open_download_folder(self):
        """Ouvre le dossier de téléchargement dans l'explorateur de fichiers"""
        folder_path = self.download_folder.get()
        if os.path.exists(folder_path):
            if platform.system() == "Windows":
                os.startfile(folder_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", folder_path])
            else:  # Linux
                subprocess.run(["xdg-open", folder_path])
        else:
            messagebox.showerror("Erreur", "Le dossier de téléchargement n'existe pas")

def main():
    """Fonction principale"""
    root = tk.Tk()
    app = DownloadGUI(root)
    
    # Centrer la fenêtre
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()